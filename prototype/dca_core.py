import asyncio
import time
from typing import List, Dict, Any

class Tier1MechanicalRouter:
    """Tier 1: O(1) Deterministic Filtering & Key Matching"""
    def __init__(self, document_store: Dict[str, str]):
        self.store = document_store

    def route_and_filter(self, query: str, target_keys: List[str]) -> tuple[str, int]:
        filtered_chunks = []
        for key in target_keys:
            if key in self.store:
                filtered_chunks.append(self.store[key])
        
        # Fallback keyword match if no explicit key match
        if not filtered_chunks:
            for k, v in self.store.items():
                if any(word.lower() in k.lower() for word in query.split()):
                    filtered_chunks.append(v)
                    
        payload = "\n".join(filtered_chunks)
        k_tokens = len(payload.split()) # Approximate token/word count (k)
        return payload, k_tokens

class Tier2AsyncRelay:
    """Tier 2: Non-blocking Out-of-Band Queue Ingestion"""
    def __init__(self):
        self.queue = asyncio.Queue()

    async def enqueue_background_document(self, key: str, content: str):
        await self.queue.put((key, content))

    async def process_queue(self, store: Dict[str, str]):
        while not self.queue.empty():
            key, content = await self.queue.get()
            store[key] = content
            self.queue.task_done()

class DCAExecutionPipeline:
    """Orchestrator combining all three tiers"""
    def __init__(self, initial_docs: Dict[str, str]):
        self.store = initial_docs
        self.router = Tier1MechanicalRouter(self.store)
        self.relay = Tier2AsyncRelay()

    async def execute(self, query: str, target_keys: List[str]) -> Dict[str, Any]:
        start_time = time.perf_counter()
        
        # 1. Process pending background queue updates (Tier 2)
        await self.relay.process_queue(self.store)
        
        # 2. Extract deterministic micro-payload (Tier 1)
        k_context, k_tokens = self.router.route_and_filter(query, target_keys)
        
        if not k_context:
            return {"error": "Payload filtered out or key not found."}

        # 3. Perform deferred reasoning (Tier 3)
        response = await self._mock_system_2_inference(query, k_context)
        
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        return {
            "query": query,
            "response": response,
            "k_tokens": k_tokens,
            "execution_time_ms": round(elapsed_ms, 2)
        }

    async def _mock_system_2_inference(self, query: str, context: str) -> str:
        await asyncio.sleep(0.05) # Simulate System-2 inference latency
        return f"DCA Reasoning Output based on filtered context: '{context}'"

# Local Execution Test
async def run_test():
    # Mock knowledge base (N total tokens)
    knowledge_base = {
        "doc_01_unrelated": "Unrelated clutter document with heavy token load. " * 50,
        "dca_complexity": "DCA isolates retrieval into Tier 1 and defers System-2 reasoning, reducing compute from O(N^2) to O(k).",
        "doc_02_unrelated": "More filler text representing raw context clutter. " * 50
    }

    pipeline = DCAExecutionPipeline(knowledge_base)
    
    # Simulate an out-of-band document update (Tier 2)
    await pipeline.relay.enqueue_background_document(
        "dca_routing", 
        "Tier 1 utilizes low-power O(1) point-to-point routing."
    )

    print("--- Running Test Query ---")
    result = await pipeline.execute(
        query="How does DCA handle context complexity?", 
        target_keys=["dca_complexity", "dca_routing"]
    )
    
    print(f"Query: {result['query']}")
    print(f"Filtered Token Count (k): {result['k_tokens']} tokens")
    print(f"Execution Latency: {result['execution_time_ms']} ms")
    print(f"Response: {result['response']}\n")

if __name__ == "__main__":
    asyncio.run(run_test())
