// Adds and retrieves data from a redis server
import { createClient } from 'redis';
const redis = require('redis');
const { promisify } = require('util');

const client = createClient();

client.on('error', (err) => console.log(
    'Redis client not connected to the server:', err));

client.on('connect', async () => {
    console.log('Redis client connected to the server');
    await main()
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
    const getAsync = promisify(client.get).bind(client);
    const value = await getAsync(schoolName);
    console.log(value);
};

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}
