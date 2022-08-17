import type { VercelRequest, VercelResponse } from '@vercel/node';
import * as dotenv from 'dotenv';
import { MongoClient } from 'mongodb';

export default (request: VercelRequest, response: VercelResponse) => {
	let ObjectId = require('mongodb').ObjectId;
	dotenv.config();
	const client = new MongoClient(process.env.MONGODB_URI || "");
	client.connect().then(() => {
		const collection = client.db("data").collection("file_stitched_paths");
		collection.find(request.body || {}).toArray().then((docs) => {
			try {
				for (let i = 0; i < docs.length; i++) {
					let body = docs[i]["body"]
					for (let j = 0; j < body.length; j++) {
						let o_id = new ObjectId(body[j]["key"]);
						docs[i]["body"][j]["key"] = client.db("data").collection("file_surgery_paths").find({_id: o_id})["new"];
					}
				}
				response.status(200).json(docs);
			} catch (err) {
				response.status(500).json({ error: err });
			}
		}).catch((err) => {
			response.status(500).json({ error: err });
		});
	}).catch((err) => {
		response.status(500).json({ error: err });
	});
	client.close();
};
