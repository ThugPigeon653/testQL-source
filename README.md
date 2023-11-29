<p align="center">
 <img src="https://images.unsplash.com/photo-1576444356170-66073046b1bc?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="TestQL - SQL unit testing made easy"></a>
</p>

<h3 align="center">TestQL - SQL unit testing made easy</h3>

<div align="center">

</div>

---

<p align = "center">💡 A CLI for creating unit tests and GitHub Actions workflows for SQL unit testing.</p>


## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Getting Started](#getting_started)
- [Commands](#commands)

See intro video: https://youtu.be/3Biv_cqomlk

## What is TestQL? <a name = "about"></a>

- This tool provides a simple solution, for unit testing SQL files before they reach your main repository. By using TestQL, you can add SQL unit tests to your repository, without actually having to provision infrastructure or write any code. 
- TestQL is a CLI tool that generates unit tests and workflows, which test SQL at the source-code level. The tool acheives this by generating all code required to test your SQL against a GitHub managed database - including provisioning of test infrastructure, dependancy management, and database connection. 
- Unit tests are generated on-demand, and run automatically every time a 'push' is made to the repository. This makes working on SQL repositories highly agile, because unit tests are being run for every commit.
- See example implementation at https://github.com/ThugPigeon653/sql-mulitilanguage


## Installation <a name = "installation"></a>

Windows:
- NOTE: A second installer will be provided soon, which does not require a python installation to run.
- Make sure you have a valid installtion of Python
- Clone the repository: https://github.com/ThugPigeon653/testQL-source.git
- Extract files: Extract files to any location you wish - the location will not affect the tools functionality
- Build and install: Run 'Build.bat' in the root of your newly extracted directory as admin

Linux:
- Coming soon... 


## Getting started <a name = "getting_started"></a>

- Create the repo: Initialize or clone a repository to a local destination of your choosing. This is the repository which does/will contain your SQL files.
- Open a terminal in the root folder of your cloned repository 
- Run the init command: 'testql init'. By default, this command will assume you are using postgres


## Commands <a name = "commands"></a>

- Note: [a,b|c] indicates that 'a' and 'b' are equivelant, while 'a' and 'c' are alternative choices.
---------------------------------------------------------------------------------
Initialize:
- testql init --engine [ postgres, pg, postgresql | tsql | mysql]
 This command sets up unit tests and a workflow file, using your chosen database engine
---------------------------------------------------------------------------------


## Contributing <a name = "contribute"></a>

Everyone is welcome to contribute at any time. I have implemented a few rules on the repository, but otherwise it is really straightforward. It is recommended to have some experience or knowledge of GitHub Actions before jumping in (and probably Python)

- Clone this repo to your desired install destination. Currently, it is installed and developed in the same location.
- Checkout a new branch (git checkout -b <branch-name>). It can be any branch, just not 'main'.
- PR: Once you have pushed some changes, open a Pull Request - thats it!

Note: Don't alter the workflow file, or push to main branch. Either of these things will automatically reject all changes.

