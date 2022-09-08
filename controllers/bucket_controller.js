var redis = require('redis');

connectRedis = async () => {
	const client = redis.createClient();

	client.on('error', (err) => console.log('Redis Client Error', err));
	client.on('connect', () => console.log('Redis Client Connected'));

	await client.connect();

	await client.set('key', 'value');
	const value = await client.get('key');
	console.log(value);
}

exports.index = (req, res) => {
	connectRedis();
	return res.sendfile('views/index.html');
}
