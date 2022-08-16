import type { VercelRequest, VercelResponse } from '@vercel/node';
import * as dotenv from 'dotenv';
import { MongoClient } from 'mongodb';

interface FileSurgeryPaths {
	current: string;
	new: string;
	redirect?: string;
	name?: string;
}

export default (request: VercelRequest, response: VercelResponse) => {
	dotenv.config();
	const client = new MongoClient(process.env.MONGODB_URI || "");
	client.connect().then(() => {
		const collection = client.db("data").collection("file_surgery_paths");
		try {
			let body = request.body;
			let tmp: FileSurgeryPaths[] = []
			for (let i = 0; i < body.data.length; i++) {
				let data: FileSurgeryPaths = {
					"current": body.data[i]["current"],  // required current path
					"new": body.data[i]["new"],  // required new path
				}
				if ("redirect" in body.data[i]) {
					data.redirect = body.data[i]["redirect"]  // optional redirect
				}
				if ("name" in body.data[i]) {
					data.name = body.data[i]["name"];  // optional name
				}
				tmp.push(data);
			}
			collection.insertMany(tmp);
			response.status(200).send(request.body);
		} catch (err) {
			response.status(400).json({ error: "bad body format" });
		}
	}).catch((err) => {
		response.status(500).json({ error: "could not connect to database" });
	});
	client.close();
};
