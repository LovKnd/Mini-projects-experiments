const { app, BrowserWindow, Menu, dialog, ipcMain, shell } = require('electron');
const fs = require('fs');
const path = require('path');

//Main Window
var mainWindow = null;
async function createWindow() {
  mainWindow = new BrowserWindow({
    width:800,
    height:600,

    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  await mainWindow.loadFile('src/pages/editor/index.html');

  //mainWindow.webContents.openDevTools();

  createNewFile();

  ipcMain.on('update-content', function(event, data){
    file.content = data;
  });
}

//File
var file = {};

//Create new file
function createNewFile(){
  file = {
    name: 'newFile.txt',
    content: '',
    saved: false,
    path: app.getPath('documents')+'/newFile.txt'
  };

  mainWindow.webContents.send('set-file', file);
}

//Save file in disk
function  writeFile(filePath){
  try{
    fs.writeFile(filePath, file.content, function(error){
      //error
      if(error) throw error;

      //Saved file
      file.path = filePath;
      file.saved = true;
      file.name = path.basename(filePath);

      mainWindow.webContents.send('set-file', file);
    })
  } catch(e){
    console.log(e);
  }
}

//Save As
async function saveFileAs(){
  //Dialog
  let dialogFile = await dialog.showSaveDialog({
    defaultPath: file.path
  });

  //Check if canceled: true
  if(dialogFile.canceled){
    return false;
  }

  //Save File
  writeFile(dialogFile.filePath);
}

//Save
function saveFile(){
    //Save File
    if(file.saved){
      return writeFile(file.path);
    }

    return saveFileAs();
}

//Read file
function readFile(filePath){
  try {
    return fs.readFileSync(filePath, 'utf8');
  } catch(e) {
    console.log(e);
    return '';
  }
}

//openFile
async function openFile(){
  //dialog
  let dialogFile = await dialog.showOpenDialog({
    defaultPath: file.path
  });

  //Check if canceled: true
  if(dialogFile.canceled) return false;

  //Open file
  file = {
    name: path.basename(dialogFile.filePaths[0]),
    content: readFile(dialogFile.filePaths[0]),
    saved: true,
    path: dialogFile.filePaths[0]
  }

  mainWindow.webContents.send('set-file', file);
}

//Template Menu
const templateMenu = [
  {
    label:'File',
    submenu: [
      {
        label:'New',
        accelerator: 'CmdOrCtrl+N',
        click(){
          createNewFile();
        }
      },
      {
        label:'Open',
        accelerator: 'CmdOrCtrl+O',
        click(){
          openFile();
        }
      },
      {
        label:'Save',
        accelerator: 'CmdOrCtrl+S',
        click(){
          saveFile();
        }
      },
      {
        label:'Save As',
        accelerator: 'CmdOrCtrl+Shift+S',
        click(){
          saveFileAs();
        }
      },
      {
        label:'Close',
        accelerator: 'CmdOrCtrl+Q',
        role:process.platform === 'darwin' ? 'close' : 'quit'
      }
    ]
  },
  {
    label: "Edit",
    submenu: [
      {
        label: 'Undo',
        role: 'undo'
      },
      {
        label: 'Redo',
        role: 'redo'
      },
      {
        type: 'separator'
      },
      {
        label: 'Copy',
        role: 'copy'
      },
      {
        label: 'Paste',
        role: 'paste'
      }
    ]
  },
  {
    label: 'More',
    submenu: [
      {
        label: 'Credits',
        click(){
          shell.openExternal('https://www.youtube.com/watch?v=rBeEvzwI11c')
        }
      },
      {
        label: 'GitHub',
        click(){
          shell.openExternal('https://github.com/LovKnd/Mini-projects-experiments/tree/main/WEB/Fogo do Doom/my-editor')
        }
      }
    ]
  }
];

//Menu
const menu = Menu.buildFromTemplate(templateMenu);
Menu.setApplicationMenu(menu);

//On Ready
app.whenReady().then(createWindow);

//Activate
app.on('activate', () => {
  if(BrowserWindow.getAllWindows().lenght === 0){
    createWindow();
  }
});
