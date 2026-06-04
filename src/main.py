from src.tools.scratchpad import Scratchpad
from src.tools.discovery import CodeTools
from src.explorer import ExplorerAgent

def run_productivity_session():
    pad = Scratchpad()
    explorer = ExplorerAgent()
    
    print("=== Initializing Developer Productivity Agent ===")
    
    # Step 1: Broad Code Discovery using Glob and Grep tools
    print("\n[Step 1] Running codebase discovery search queries...")
    files = CodeTools.glob_search("*.ts")
    print(files[0])
    
    matches = CodeTools.grep_search("verifyToken")
    print(matches[0])
    
    # Step 2: Delegate complex file to Deep-Dive Explorer Subagent
    print("\n[Step 2] Spawning Explorer Agent to perform context-isolated deep dive...")
    analysis_result = explorer.deep_dive("src/auth.ts")
    
    # Step 3: Append finding securely to the persistent Scratchpad file
    print("\n[Step 3] Committing key architecture logs to scratchpad backend...")
    save_msg = pad.append_finding(analysis_result)
    print(save_msg)
    
    print("\n=== Workspace Analysis Completed Successfully ===")

if __name__ == "__main__":
    run_productivity_session()