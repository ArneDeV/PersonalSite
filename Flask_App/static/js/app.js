// Checkt of browser service workers support
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('./service-worker.js')
        .then((regstration) => console.log('Service Worker registrated!', regstration)) // Async functie succesvol
        .catch((err) => console.log('Registation of service worker failed!', err)); // async functie onsuccesvol
};