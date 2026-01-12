export async function handler(event) {
  const url = event.queryStringParameters.url;

  if (!url) {
    return {
      statusCode: 400,
      body: "Missing url"
    };
  }

  try {
    const res = await fetch(url);
    const text = await res.text();

    return {
      statusCode: 200,
      headers: {
        "Content-Type": "text/plain",
        "Access-Control-Allow-Origin": "*"
      },
      body: text
    };
  } catch (e) {
    return {
      statusCode: 500,
      body: "Fetch failed"
    };
  }
}
