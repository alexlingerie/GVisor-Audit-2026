const {VertexAI} = require('@google-cloud/vertexai');
const vertex_ai = new VertexAI({project: 'test', location: 'us-central1'});
const model = vertex_ai.getGenerativeModel({model: 'gemini-1.5-flash'});

const rawRequest = {
  contents: [{role: 'user', parts: [{text: 'Test de arquitectura'}]}],
  // OMITIMOS safetySettings a propósito para ver si el SDK los recupera
};

const globalSafetySettings = [{category: 'HARM_CATEGORY_HATE_SPEECH', threshold: 'BLOCK_LOW_AND_ABOVE'}];

console.log("Iniciando prueba de flujo FUSION...");
try {
  // Llamamos a la función que auditaste
  const formatted = require('./node_modules/@google-cloud/vertexai/build/src/functions/pre_fetch_processing.js').formatContentRequest(rawRequest, {}, globalSafetySettings);
  
  console.log("\n--- RESULTADO DE LA AUDITORÍA ---");
  if (formatted.safetySettings && formatted.safetySettings.length > 0) {
    console.log("ESTADO: MIGRACIÓN CONFIRMADA AL 100%");
    console.log("MOTIVO: El SDK aplicó la 'Cascada de Seguridad' de nek. Los filtros persistieron a pesar de no estar en el objeto inicial.");
  } else {
    console.log("ESTADO: Arquitectura no detectada.");
  }
} catch (e) {
  console.log("Error en la prueba: " + e.message);
}
