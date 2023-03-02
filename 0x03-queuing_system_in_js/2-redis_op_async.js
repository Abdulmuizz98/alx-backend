import * as redis from 'redis';
import util from 'util';

const client = redis.createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err.message));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value){
  client.set(schoolName, value, redis.print);
}

const get = util.promisify(client.get).bind(client);

async function displaySchoolValue(schoolName){
  const value = await get(schoolName);
  console.log(value);
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})()
