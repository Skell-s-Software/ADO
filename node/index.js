const { app, BrowserWindow } = require('electron');

function crearVentana() {
    const ventana = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            webviewTag: true
        }
    });
    ventana.loadURL('http://192.168.0.102:8501');
}

app.whenReady()
.then(
    crearVentana
);