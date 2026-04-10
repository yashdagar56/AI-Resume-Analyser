/**
 * API Configuration
 * 
 * This file helps the frontend decide which backend URL to use.
 * - If running locally (localhost or 127.0.0.1), it uses the local backend.
 * - Otherwise, it uses the production backend URL.
 */

const API_CONFIG = {
    // 1. CHANGE THIS to your actual Railway/Render/Production URL once you have it!
    // Example: "https://ai-resume-analyser-production.up.railway.app"
    productionUrl: "https://your-production-url-here.up.railway.app",
    
    localUrl: "http://localhost:8000",
    
    // Automatically determine which base URL to use
    get baseUrl() {
        const isLocal = window.location.hostname === "localhost" || 
                        window.location.hostname === "127.0.0.1";
        
        // If we have a placeholder production URL, we might want to alert the user or fallback
        if (!isLocal && this.productionUrl.includes("your-production-url-here")) {
            console.warn("Production URL is still using the placeholder. Please update api-config.js");
        }
        
        return isLocal ? this.localUrl : this.productionUrl;
    }
};

window.API_CONFIG = API_CONFIG;
