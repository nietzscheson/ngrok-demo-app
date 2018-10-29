const http = require('http');
const PORT = 4390;

function handleRequest(request, response) {
  response.end('Ngrok is working! -  Path Hit: ' + request.url);
}

const server = http.createServer(handleRequest);

server.listen(PORT, function () {
  console.log("Server listening on: http://localhost:%s", PORT);
});