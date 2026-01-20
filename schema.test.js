const Ajv = require('ajv');
const fs = require('fs').promises;
const path = require('path');

describe('Schema Validation Tests', () => {
  let ajv;
  let validate;


  beforeAll(async () => {
    const schemaPath = path.join(__dirname, 'vega-lite-protoschema.json');
    const schemaData = await fs.readFile(schemaPath, 'utf8');
    const schema = JSON.parse(schemaData);
    
    ajv = new Ajv();
    validate = ajv.compile(schema);
  });

  test('example-json-1.json validation', async () => {
    const filePath = path.join(__dirname, 'example-json-1.json');
    const fileData = await fs.readFile(filePath, 'utf8');
    const datafile = JSON.parse(fileData);
    
    const valid = validate(datafile);
    
    if (!valid) {
      console.error('Validation errors:', validate.errors);
    }
    
    expect(valid).toBe(true);
    expect(validate.errors).toBeNull();
  });

  test('example-json-2.json validation', async () => {
    const filePath = path.join(__dirname, 'example-json-2.json');
    const fileData = await fs.readFile(filePath, 'utf8');
    const datafile = JSON.parse(fileData);
    
    const valid = validate(datafile);
    
    if (!valid) {
      console.error('Validation errors:', validate.errors);
    }
    
    expect(valid).toBe(true);
    expect(validate.errors).toBeNull();
  });


});
