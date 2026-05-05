import asyncio
from typing import Dict

# resource storage with type annotation
resources: Dict[int, Dict[str, object]] = {
    501: {"title": "Basic Physics", "available": True},
    502: {"title": "Intro to AI", "available": True}
}

async def issue_resource(student_id: int, resource_id: int) -> str:
    print(f"Issuing resource {resource_id}...")
    await asyncio.sleep(1)

    if resources[resource_id]["available"]:
        resources[resource_id]["available"] = False
        return f"Student {student_id} successfully issued resource {resource_id}"
    
    return "Resource not available"

async def submit_resource(student_id: int, resource_id: int) -> str:
    print(f"Submitting resource {resource_id}...")
    await asyncio.sleep(1)

    resources[resource_id]["available"] = True
    return f"Student {student_id} submitted resource {resource_id}"

async def run_system() -> None:
    task_a: asyncio.Task = asyncio.create_task(issue_resource(9001, 501))
    task_b: asyncio.Task = asyncio.create_task(issue_resource(9002, 502))
    task_c: asyncio.Task = asyncio.create_task(submit_resource(9001, 501))

    results = await asyncio.gather(task_a, task_b, task_c)

    print("\n--- Results ---")
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(run_system())
