import type { VercelRequest, VercelResponse } from '@vercel/node';
import * as dotenv from 'dotenv';
import { MongoClient } from 'mongodb';

interface FileMovePaths {
	current: string;
	new: string;
	name?: string;
}

export default (request: VercelRequest, response: VercelResponse) => {
	dotenv.config();
	const client = new MongoClient(process.env.MONGODB_URI || "");
	client.connect().then(() => {
		const db = client.db("data");
		const collection = db.collection("file_move_paths");
		try {
			let body = JSON.parse(request.body);
			/*for (let i = 0; i < body.data.length; i++) {
				let data: FileMovePaths = {
					"current": body.data[i]["current"],  // required current path
					"new": body.data[i]["new"]  // required new path
				}
				if ("name" in body.data[i]) {
					data.name = body.data[i]["name"];  // optional name
				}
				collection.insertOne(data);
			}*/
			response.status(200).send(body);
		} catch (err) {
			response.status(400).json({ error: "bad body format" });
		}
	}).catch((err) => {
		response.status(500).json({ error: "could not connect to database" });
	});
};
