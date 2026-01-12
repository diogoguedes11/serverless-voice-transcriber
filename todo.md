INICIAR Função(evento):

1. LER dados do evento (JSON): ✅
   -> Qual é o nome do bucket? (ex: "input-bucket") ✅
   -> Qual é o nome do ficheiro? (ex: "reuniao.mp3") ✅

2. VALIDAR: ✅
   -> É mesmo um ficheiro de áudio? (Para não processar .txt ou pastas) ✅

3. PREPARAR input para a IA:
   -> Criar o caminho GCS: "gs://input-bucket/reuniao.mp3" ✅
   -> Criar o objeto "Part" do Vertex AI (é assim que se envia ficheiros para o Gemini).

4. CHAMAR O GEMINI (Vertex AI):
   -> Modelo: "gemini-1.5-flash-001" (Rápido e barato)
   -> Prompt: "Transcreve este áudio e cria um sumário em tópicos."
   -> Enviar Audio + Prompt.

5. PROCESSAR Resposta:
   -> Receber o texto gerado.

6. GUARDAR Resultado:
   -> Definir nome do ficheiro de saída (ex: "reuniao.txt")
   -> Ligar ao Bucket de Saída ("output-bucket")
   -> Escrever o texto lá.

7. FINALIZAR:
   -> Print de sucesso.
