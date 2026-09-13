
document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const mainNav = document.getElementById('mainNav');

    // Mobile Menu
    if(mobileBtn && mainNav) {
        mobileBtn.addEventListener('click', () => {
            mainNav.classList.toggle('show');
        });
    }
});


// --- Client-Side Search Implementation ---
const searchIndex = [{"title": "Cloud Computing Explained: IaaS, PaaS, and SaaS", "url": "cloud-computing-explained.html"}, {"title": "Computer Networks Explained: LAN, WAN, and Wi-Fi Basics", "url": "computer-networks-explained.html"}, {"title": "Computer Vision: How Machines and Computers See the World", "url": "computer-vision-how-machines-see.html"}, {"title": "How Computer Memory Works: RAM, ROM, and Storage Explained", "url": "computer-memory-and-storage.html"}, {"title": "How Machine Learning Works: A Simple Beginner's Guide", "url": "how-machine-learning-works.html"}, {"title": "How Search Engines Work & SEO Basics Explained", "url": "how-search-engines-work.html"}, {"title": "How the Internet Works: A Complete Guide", "url": "how-the-internet-works.html"}, {"title": "Introduction to Computers: A Complete Beginner's Guide", "url": "introduction-to-computers.html"}, {"title": "Introduction to Cybersecurity: Firewalls & Encryption", "url": "cybersecurity-fundamentals-explained.html"}, {"title": "Natural Language Processing (NLP) Explained Simply", "url": "natural-language-processing-explained.html"}, {"title": "Operating Systems Explained: Windows, macOS, and Linux", "url": "operating-systems-explained.html"}, {"title": "The Difference Between Frontend and Backend Web Development", "url": "frontend-vs-backend-development.html"}, {"title": "The Impact of Artificial Intelligence on the Healthcare Industry", "url": "ai-impact-on-healthcare.html"}, {"title": "Top 5 Uses of Automation to Boost Daily Productivity", "url": "automation-to-boost-productivity.html"}, {"title": "Two-Factor Authentication (2FA) Explained: A Security Must-Have", "url": "two-factor-authentication-explained.html"}, {"title": "Understanding End-to-End Encryption in Messaging Apps", "url": "understanding-end-to-end-encryption.html"}, {"title": "What Is Edge Computing", "url": "what-is-edge-computing.html"}, {"title": "What is 6G Technology? The Ultimate Guide", "url": "what-is-6g-technology.html"}, {"title": "What is Artificial Intelligence? ML vs Deep Learning", "url": "what-is-artificial-intelligence.html"}, {"title": "What is Quantum Computing? The Ultimate Guide", "url": "what-is-quantum-computing.html"}, {"title": "What is Web 3.0? The Complete Beginner's Guide", "url": "what-is-web3-explained.html"}, {"title": "What is a Database? SQL vs NoSQL Explained", "url": "what-is-a-database-sql-vs-nosql.html"}, {"title": "What is a Password Manager? Your Guide to Smarter Digital Account Management", "url": "what-is-a-password-manager.html"}, {"title": "What is an API? Explained in Simple Terms", "url": "what-is-an-api-explained.html"}];

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    
    if(searchInput && searchResults) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            if(query.length < 2) {
                searchResults.style.display = 'none';
                return;
            }
            
            const matches = searchIndex.filter(item => item.title.toLowerCase().includes(query));
            
            if(matches.length > 0) {
                searchResults.innerHTML = matches.map(m => `
                    <a href="${m.url}" style="display: block; padding: 12px 15px; border-bottom: 1px solid var(--border-color); text-decoration: none; color: var(--text-main); font-weight: 500; font-size: 0.95rem; transition: background 0.2s;">
                        ${m.title}
                    </a>
                `).join('');
                searchResults.style.display = 'block';
            } else {
                searchResults.innerHTML = `<div style="padding: 15px; color: var(--text-light); text-align: center;">No results found</div>`;
                searchResults.style.display = 'block';
            }
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if(!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                searchResults.style.display = 'none';
            }
        });
    }
});
