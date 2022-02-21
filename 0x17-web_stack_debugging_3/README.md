# 0x17. Web stack debugging #3

## Background Context

### Six Stages of Debugging

* That can't happen.
* That doesn't happen on my machine.
* That shouldn't happen.
* Why does that happen?
* Oh, I see. 
* How did that ever work?

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something ALX students can do :)

## Requirements

### General

* All your files will be interpreted on Ubuntu 14.04 LTS.
* All your files should end with a new line.
* A README.md file at the root of the folder of the project is mandatory.
* Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
* Your Puppet manifests must run without error.
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
* Your Puppet manifests files must end with the extension .pp.
* Files will be checked with Puppet v3.4.

## More Info

### Install `puppet-lint`

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1 
```

## Author

Joseph Mahiuha - [Github](https://github.com/Mahiuha) / [Twitter](https://twitter.com/Joseph_Mahiuha)
