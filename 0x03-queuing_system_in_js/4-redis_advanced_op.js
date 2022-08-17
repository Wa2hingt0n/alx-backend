// Stores hash values
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const fields = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
};

for (const [key, value] of Object.entries(fields)) {
    client.hset('HolbertonSchools', key, value, print);
}

client.hgetall('HolbertonSchools', (err, reply) => {
    console.log(reply);
});
