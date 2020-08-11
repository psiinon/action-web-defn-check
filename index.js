const core = require('@actions/core');
const github = require('@actions/github');

try {
  console.log(`Testing 1 2 3 !`);
} catch (error) {
  core.setFailed(error.message);
}
