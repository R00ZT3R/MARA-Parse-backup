const express = require("express");
const app = express();
const port = 8000;

const TEST_COMMAND = `python3 -c 'print("Hello world")'`;
const GET_QUESTIONS = `conda activate pytorch-test && conda run python3 question_generator.py`;

const command = (commandStr) => {
  let { exec } = require("child_process");
  return new Promise((resolve) => {
    const res = exec(commandStr, (error, stdout, stderr) => {
      resolve({ stdout, stderr, error });
    });
  });
};

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/questions", async (req, res) => {
  const result = await command(GET_QUESTIONS);
  console.log(result);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
