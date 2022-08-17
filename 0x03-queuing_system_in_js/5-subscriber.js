// Creates a redis client that subscribes to a channel and receives messages
import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.SUBSCRIBE('holberton school channel');

subscriber.on('message', (_channel, message) => {
    if (message === 'KILL_SERVER') {
	console.log(message);
	subscriber.unsubscribe();
	subscriber.quit();
    } else {
	console.log(message);
    }
});
