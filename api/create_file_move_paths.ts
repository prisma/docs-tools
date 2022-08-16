import type { VercelRequest, VercelResponse } from '@vercel/node';
import * as dotenv from 'dotenv';
import { MongoClient } from 'mongodb';

export default (request: VercelRequest, response: VercelResponse) => {
	dotenv.config();
	const client = new MongoClient(process.env.MONGODB_URI || "");
	client.connect().then(() => {
		const db = client.db("data");
		const collection = db.collection("file_move_paths");
		try {
			let body = JSON.parse(request.body);
			for (let i = 0; i < body.data.length; i++) {
				let data = {
					"current": body.data[i]["current"],  // required current path
					"new": body.data[i]["new"]  // required new path
				}
				if ("name" in body["data"][i]) {
					data["name"] = body.data[i]["name"];  // Optional name
				}
				collection.insertOne(data);
			}
		} catch (err) {
			response.status(500).json({ error: err });
		}
	}).catch((err) => {
		response.status(500).json({ error: err });
	});
};
