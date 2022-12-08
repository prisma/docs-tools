use http::{StatusCode};
use vercel_lambda::{lambda, error::VercelError, IntoResponse, Request, Response};
use std::error::Error;
use passtoken::{init_auth, login};
use std::env;

async fn handler(_: Request) -> Result<impl IntoResponse, VercelError> {
	let auth = init_auth(env::var("POSTGRES_URL").unwrap(), env::var("REDIS_URL").unwrap()).await.unwrap();
	let token = login(&auth, Request.headers().get("email").unwrap().to_str().unwrap(), Request.headers().get("password").unwrap().to_str()).await.unwrap();

	let response = Response::builder()
		.status(StatusCode::OK)
		.header("Content-Type", "text/plain")
		.body(token)
		.expect("Internal Server Error");

		Ok(response)
}

// Start the runtime with the handler
fn main() -> Result<(), Box<dyn Error>> {
	Ok(lambda!(handler))
}