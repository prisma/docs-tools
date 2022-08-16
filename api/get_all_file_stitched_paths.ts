import type { VercelRequest, VercelResponse } from '@vercel/node';
import * as dotenv from 'dotenv';
import { MongoClient } from 'mongodb';

export default (request: VercelRequest, response: VercelResponse) => {
	dotenv.config();
	const client = new MongoClient(process.env.MONGODB_URI || "");
	client.connect().then(() => {
		const db = client.db("data");
		const collection = db.collection("file_stitched_paths");
		collection.find({}).toArray().then((docs) => {
			response.status(200).json(docs);
		}).catch((err) => {
			response.status(500).json({ error: err });
		});
	}).catch((err) => {
		response.status(500).json({ error: err });
	});
};
