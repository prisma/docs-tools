import type { VercelRequest, VercelResponse } from '@vercel/node';
import * as dotenv from 'dotenv';
import { MongoClient } from 'mongodb';

export default (request: VercelRequest, response: VercelResponse) => {
	dotenv.config();
	const client = new MongoClient(process.env.MONGODB_URI || "");
	client.connect().then(() => {
		const collection = client.db("data").collection("file_stitched_paths");
		collection.find(request.body || {}).toArray().then((docs) => {
			try {
				for (let i = 0; i < docs.length; i++) {
					let body = docs[i]["body"]
					for (let j = 0; j < body.length; j++) {
						docs[i]["body"][j]["key"] = client.db("data").collection("file_surgery_paths").findOne({"_id": body[j]["key"]})["new"];
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
