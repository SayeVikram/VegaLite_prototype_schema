

const Ajv = require('ajv');
const arr = ['./example-json-1.json', './example-json-2.json'];

fs = require('fs')
fs.readFile('./vega-lite-protoschema.json', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  //console.log(data);

  const ajv = new Ajv();
  const schema = JSON.parse(data);

  const validate = ajv.compile(schema);



  fs.readFile(arr[0], 'utf8', function (err,file) { //modify arr index to check validity of other file
    if (err) {
        return console.log(err);
    }

    const datafile = JSON.parse(file);
    const valid = validate(datafile);


    if(!valid) console.log("FAILED");
    else console.log("Successfully validated");
    console.log(validate);

  });

});