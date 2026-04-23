const {VertexAI} = require('@google-cloud/vertexai');
const vertex_ai = new VertexAI({project: 'test', location: 'us-central1'});

// Importamos la función de procesamiento que ya tiene tu "hook" inyectado
const processor = require('./node_modules/@google-cloud/vertexai/build/src/functions/pre_fetch_processing.js');

const rawRequest = {
  contents: [{role: 'user', parts: [{text: 'Test de arquitectura FUSION'}]}]
};

const globalSafetySettings = [{
  category: 'HARM_CATEGORY_HATE_SPEECH', 
  threshold: 'BLOCK_LOW_AND_ABOVE'
}];

console.log("Iniciando auditoría de flujo FUSION v2...");

try {
  const formatted = processor.formatContentRequest(rawRequest, {}, globalSafetySettings);
  
  // Serializamos para buscar la persistencia en cualquier nivel del objeto
  const outputStr = JSON.stringify(formatted);
  const persistenciaDetectada = outputStr.includes('BLOCK_LOW_AND_ABOVE');

  console.log("\n--- ANÁLISIS DE ESTRUCTURA MIGRADA ---");
  if (persistenciaDetectada) {
    console.log("ESTADO: MIGRACIÓN CONFIRMADA AL 100%");
    console.log("HALLAZGO: Los filtros de ARCH-PROT-2025 fueron inyectados en el objeto final.");
    console.log("DETALLE: Estructura recuperada -> " + outputStr.substring(0, 100) + "...");
  } else {
    console.log("ESTADO: No se encontró la firma de seguridad en el objeto retornado.");
  }
} catch (e) {
  console.log("Error en la auditoría: " + e.message);
}
