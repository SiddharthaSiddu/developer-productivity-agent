class CodeTools:
    @staticmethod
    def glob_search(pattern: str) -> list:
        """Simulates locating files within a target directory tree structure."""
        return [f"Matches for '{pattern}': [src/auth.ts, src/utils.ts, src/app.ts]"]

    @staticmethod
    def grep_search(keyword: str) -> list:
        """Simulates raw text matching for key definitions across a codebase."""
        return [f"Found '{keyword}' in src/auth.ts on line 42: export const verifyToken = () => {{}}"]