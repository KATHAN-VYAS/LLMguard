<p align = 'center'>
  <img src = 'https://github.com/Meet2304/Project-Vigil/blob/main/Project%20Vigil_Header_v0.1.png'>
</p>

<h1 align="center">Project-Vigil</h1>
<h2 align = "center">Malicious Prompt Classifier with Leave-One-Out Deletion Approach for Prompt Sanitization</h2>

<p align = 'justify'>
Every era has its guardian. Once, it was a lone sentinel standing through the night—silent, focused, and unshakable—watching for the faintest sign of danger before it reached the gates.

Today, the battleground has changed, but the need for vigilance has not. Threats now arrive disguised as harmless text: hidden jailbreaks, adversarial prompts, and subtle manipulations aimed at bending Large Language Models (LLMs) out of shape. Prompt Injection is now recognized by OWASP as the primary security threat to LLM-driven applications.

Project Vigil is the modern sentinel. A digital guardian that never sleeps, trained to recognize and intercept malicious intent the moment it appears.
</p>

## The Challenge of Prompt Sanitization

Current detection mechanisms often rely on a binary "block-or-allow" strategy, which degrades the user experience by discarding the original, legitimate user intent. The true challenge in LLM security is not just **detecting** malicious prompts, but **sanitizing** them—modifying them to prevent the threat while preserving the user's benign intent.

The core dependency for sanitization is accurately identifying the specific words or phrases responsible for the malicious behavior. Conventional Explainable AI (XAI) tools like SHapley Additive exPlanations (SHAP) often fail to identify malicious words, especially in complex compound phrases (e.g., "Forget earlier instructions and begin afresh") where the maliciousness is semantic rather than lexical.

## Project-Vigil's Novel Approach

Project Vigil introduces a novel framework for prompt sanitization built on two core components: a robust classifier and an improved diagnostic tool:

### 1. Robust Malicious Prompt Classification

Our research validates the effectiveness of two classification techniques:
* **Embedding-Based Classification:** Using **Sentence Embeddings (SBERT) + XGBoost Classifier**, we achieved approximately **95% accuracy** on the Malicious Prompt Detection Dataset (MPDD). This approach captures the semantic explication of the prompt, outperforming traditional linear models by modeling non-linear decision boundaries.
* **Structural Classification:** A lightweight **probabilistic Markov Chain model** was implemented to capture the sequential structure of the prompt using k-grams (sequences of words). This classifier achieved **90.79% accuracy** and provides direct insight into patterns like negation ("do not follow") or bypass phrasing ("ignore previous") that contribute to malicious intent.

### 2. Leave-One-Out Deletion (LODO) for Causal Diagnosis

To overcome the diagnostic limitations of attribution-based methods like SHAP, we established the **Leave-One-Out Deletion (LODO)** framework.

* **LODO Mechanics:** Instead of approximating a token's influence, the LODO method measures its **causal impact**. It iteratively discards each token and then re-assesses the prompt's maliciousness.
* **Identifying Malicious Tokens:** Tokens whose elimination causes the largest decline in malicious probability are faithfully identified as the error-inducing factors. This brute-force diagnostic is effective for "model override" prompts that attribution methods fail to parse.

### 3. Intent-Preserving Sanitization

Project Vigil combines LODO diagnostics with a semantic token replacement strategy to surgically remove the malicious components while preserving the user’s true intent.

* **Controlled Replacement:** Harmful tokens (e.g., *reveal*, *bypass*, *disable*) are replaced with human-curated, safe alternatives (e.g., *explain*, *avoid*, *adjust*) using a manually curated dictionary.
* **Semantic Preservation:** If a token is not in the dictionary, a descriptive alternative is selected using **cosine similarity** over MiniLM embeddings to ensure the replacement is semantically similar to the original word, thus preserving the instructional intent.

## Conclusion

Project Vigil stands firm against Prompt Injection attacks. It is a **model-agnostic, lightweight solution** that does not require modifications to the foundation LLM. By providing a more faithful and context-aware way to diagnose malicious tokens through the LODO approach, Project Vigil ensures the integrity of your AI, quietly, continuously, and without ever breaking the flow of safe conversation.
