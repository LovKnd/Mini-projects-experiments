const { ipcRenderer } = require('electron');

//Elements
const textarea = document.getElementById('text');
const title = document.getElementById('title');

//Set file
ipcRenderer.on('set-file', function(event, data){
  textarea.value = data.content;
  title.innerHTML = data.name+ ' | MyEditor';
});

//Update textArea
function handleChangeText(){
  ipcRenderer.send('update-content', textarea.value);
}
