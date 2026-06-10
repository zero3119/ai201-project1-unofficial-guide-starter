import gradio as gr
from query import ask


def handle_query(question):
    result = ask(question)

    sources = "\n".join(f"• {source}" for source in result["sources"])

    chunks = "\n\n---\n\n".join(
        f"Source: {chunk['source']}\n"
        f"Chunk ID: {chunk.get('chunk_id', 'N/A')}\n\n"
        f"{chunk['text']}"
        for chunk in result["chunks"]
    )

    return result["answer"], sources, chunks


with gr.Blocks() as demo:
    gr.Markdown("# UTEP Food Guide Assistant")

    question = gr.Textbox(label="Your question")
    btn = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    chunks = gr.Textbox(label="Retrieved chunks", lines=12)

    btn.click(handle_query, inputs=question, outputs=[answer, sources, chunks])
    question.submit(handle_query, inputs=question, outputs=[answer, sources, chunks])


demo.launch()