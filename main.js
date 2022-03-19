const { app, BrowserWindow } = require('electron')
const path = require('path')

function createWindow () {
  const win = new BrowserWindow({
    width: 1200,
    height: 900,
    icon: '/home/xplore/Desktop/Xplore/Icons/Xplore-logo.icns',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })
  win.removeMenu(true)
  
  win.loadURL('http://127.0.0.1:8000/launcher/')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
