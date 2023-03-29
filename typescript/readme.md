Download and install node:
https://nodejs.org/en/download

Install typescript:

`npm install -g typescript`

To transpile:

`tsc Basics.ts`

To run the transpiled file:

`node Basics.js`



Specify compiler options:
```json
{
    "compilerOptions": {
      "target": "es5",
      "module": "commonjs",
      "sourceMap": true,
      "rootDir": "src",
      "outDir": "dist"
    }
  }
```

Ensure the folders exist. After that, compile everything using:
```
tsc
node .\dist\xxx.js
node .\dist\Basics.js
```