# Comparativa de Arquitectura: Vertex AI vs. Google GenAI
**Investigador:** Víctor Hugo Obando González (nek)
**Protocolo:** ARCH-PROT-2025 / FUSION v2.0

## 1. Mapeo de Funciones Críticas (Vertex AI SDK)
export declare function formatContentRequest(request: GenerateContentRequest | string, generationConfig?: GenerationConfig, safetySettings?: SafetySetting[]): GenerateContentRequest;
export declare function validateGenerateContentRequest(request: GenerateContentRequest): void;
export declare function validateGenerationConfig(generationConfig: GenerationConfig): GenerationConfig;
export declare function getApiVersion(request: GenerateContentRequest): 'v1' | 'v1beta1';
export declare function hasVertexRagStore(request: GenerateContentRequest): boolean;
export declare function hasVertexAISearch(request: GenerateContentRequest): boolean;

## 2. Definiciones de Seguridad (GenAI SDK)
    safetySettings?: SafetySetting[];
    BLOCK_LOW_AND_ABOVE = "BLOCK_LOW_AND_ABOVE",
    safetySettings?: SafetySetting[];
    safetySettings?: SafetySetting[];
    BLOCK_LOW_AND_ABOVE = "BLOCK_LOW_AND_ABOVE",
    BLOCK_LOW_AND_ABOVE = "BLOCK_LOW_AND_ABOVE",
/** A safety setting that affects the safety-blocking behavior. A SafetySetting consists of a harm category and a threshold for that category. */
export declare interface SafetySetting {
        SafetySetting,

## 3. Punto de Inyección de Lógica (GVisor-Audit-Fix)


## 4. Correlación de Dependencias
GVisor-Audit-2026@ /data/data/com.termux/files/home/GVisor-Audit-2026
├─┬ @google-cloud/vertexai@1.12.0
│ └── @google/genai@1.50.1 deduped
└── @google/genai@1.50.1
