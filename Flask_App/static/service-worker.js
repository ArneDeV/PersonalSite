const staticCacheName = 'static-files';
const chacheAssets = [
    '/',
    '/home',
    '/blog',
    '/photos',
    '/static/js/app.js',
    '/static/js/photos.js',
    '/static/forms.css',
    '/static/main.css',
    'https://fonts.googleapis.com/css2?family=Poppins:wght@500;700&display=swap',
];

// 1. Install service worker
self.addEventListener('install', evt => {
    evt.waitUntil(
        caches.open(staticCacheName).then(cache => {
            console.log("Caching assets!")
            cache.addAll(chacheAssets);
        })
    );
});

// Activate service worker
self.addEventListener('activate', evt => {
    console.log("Service worken has been activated");
});

// Fetch events (Haalt iets van server, laden pagina, ...)
self.addEventListener('fetch', (evt) => {
    // console.log("Fetch event", evt); //* printen van events
});