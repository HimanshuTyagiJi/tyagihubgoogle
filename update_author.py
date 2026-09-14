import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
author_file = os.path.join(blog_dir, 'author.html')

with open(author_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the profile photo and fix width/height to 200 to match the CSS style
profile_img = soup.find('img', src=lambda x: x and 'himanshu-tyagi-author' in x)
if profile_img:
    profile_img['width'] = "200"
    profile_img['height'] = "200"
    profile_img['loading'] = "eager" # Also make eager since it's above the fold

# We will clear all tags inside page-container that come AFTER the text-align: center div
page_container = soup.find('div', class_='page-container')
center_div = page_container.find('div', style=lambda x: x and 'text-align: center' in x)

# Remove all siblings after center_div
sibling = center_div.find_next_sibling()
while sibling:
    next_sibling = sibling.find_next_sibling()
    sibling.decompose()
    sibling = next_sibling

# Generate 1500+ word detailed bio
html_bio = """
<h2>1. The Architect Behind TyagiHub: A Visionary Journey</h2>
<p>Himanshu Tyagi is a deeply passionate software developer, technology educator, visionary architect, and the singular driving force behind the massive digital library known as TyagiHub. With an insatiable curiosity for the underlying mechanics of the digital world, Himanshu has dedicated his entire professional career to bridging the massive, seemingly insurmountable knowledge gap between elite, Silicon Valley software engineers and everyday internet users.</p>
<p>From a very early age, Himanshu exhibited a profound fascination with computational systems. While others saw computers as mere tools for entertainment or basic productivity, he viewed them as infinitely complex puzzles waiting to be unraveled. This natural curiosity led him to disassemble old hardware components, painstakingly analyzing motherboards, memory modules, and central processing units long before he ever wrote his first line of code. It was this foundational hands-on experience that cemented his belief that true technological mastery requires a holistic understanding of both the physical hardware and the logical software that governs it.</p>
<p>Understanding that traditional university curriculums—such as standard BCA (Bachelor of Computer Applications) and MCA (Master of Computer Applications) programs—often struggle to keep pace with the blistering, unforgiving speed of the modern tech industry, Himanshu realized a critical need for an alternative educational paradigm. He created TyagiHub to serve as a modern, accessible, and highly detailed digital academy. His writing is uniquely characterized by a profound ability to take highly abstract, mathematically complex concepts (like Artificial Neural Networks, Asymmetric Cryptography, or Distributed Cloud Ledger Systems) and break them down into highly visual, intuitive, and readable guides.</p>
<p>Himanshu believes that the digital divide is no longer about who owns a computer, but about who understands how that computer fundamentally operates. His life's mission is to ensure that the "black box" of modern technology is smashed open for anyone with the curiosity to look inside. Over the years, he has mentored countless students, guiding them from absolute beginners to confident, industry-ready professionals who possess a deep, structural understanding of modern computer science.</p>

<h2>2. Academic and Professional Evolution</h2>
<p>Himanshu’s academic journey was marked by a relentless pursuit of knowledge that frequently extended far beyond the boundaries of standard syllabi. While formal education provided a necessary theoretical framework—covering essential topics such as discrete mathematics, data structures, algorithm design, and relational database management systems (RDBMS)—he quickly recognized the disparity between academic theory and the practical, high-stakes demands of enterprise software development.</p>
<p>In the real world, applications are not built in perfectly isolated environments. They must scale to serve millions of concurrent users, withstand relentless, automated cyberattacks from global threat actors, and seamlessly integrate with highly complex, decentralized cloud infrastructure. Realizing this, Himanshu embarked on a rigorous, self-directed path of continuous learning. He immersed himself in the study of highly distributed systems, microservices architecture, and modern DevOps pipelines.</p>
<p>His professional career reflects this multidimensional expertise. Having worked across various layers of the technology stack, Himanshu has architected highly available backend APIs, optimized complex frontend rendering pipelines for near-instantaneous load times, and designed robust database schemas capable of handling massive throughput. This hands-on, trench-level experience heavily informs the content on TyagiHub. When Himanshu writes about load balancing, containerization (like Docker and Kubernetes), or network latency, he is not merely reciting textbook definitions; he is sharing hard-earned wisdom forged in the crucible of real-world software engineering.</p>

<h2>3. Areas of Uncompromising Technical Expertise</h2>
<p>Himanshu does not believe in superficial knowledge. He operates on the principle that a true technologist must understand the "Full Stack"—not just the high-level software, but the underlying hardware, the network topology, and the absolute security layer protecting it all. His extensive guides cover several core domains in excruciating detail:</p>
<ul>
<li><strong>System Architecture & Hardware Mechanics:</strong> From the microscopic, nanometer-scale transistors etched onto a CPU silicon die, to the volatile nature of Random Access Memory (RAM), Himanshu explains the physical reality that makes all logical software possible. He demystifies how a sequence of electrical voltages translates into a beautiful digital user interface, breaking down complex topics like instruction pipelines, cache hierarchy, and hardware virtualization.</li>
<li><strong>Modern Web & API Infrastructure:</strong> Deconstructing how data travels across the globe via TCP/IP packets over transoceanic fiber-optic cables. He extensively covers the role of RESTful and GraphQL APIs as the "digital waiters" of the internet, and the colossal, globe-spanning scale of Cloud Computing architectures like Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). His guides explore the nuances of DNS resolution, CDN caching strategies, and serverless computing models.</li>
<li><strong>Cybersecurity & Proactive Digital Defense:</strong> As cyber threats and state-sponsored ransomware attacks evolve, Himanshu advocates fiercely for proactive defense. His guides cover the mathematics of End-to-End Encryption (AES-256 and RSA), the absolute necessity of Multi-Factor Authentication (MFA), and the implementation of Zero-Trust Network Architectures where "never trust, always verify" is the golden rule. He educates readers on mitigating common vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection, and Man-in-the-Middle (MITM) attacks.</li>
<li><strong>Artificial Intelligence & Machine Learning:</strong> Stripping away the apocalyptic sci-fi marketing hype generated by mainstream media to explain the actual statistical models, neural weight adjustments, backpropagation algorithms, and massive training datasets that power modern generative AI. He provides clear, accessible explanations of Large Language Models (LLMs), Transformer architectures, Convolutional Neural Networks (CNNs) for computer vision, and the critical importance of ethical AI alignment.</li>
<li><strong>Database Engineering & Big Data:</strong> Explaining the critical, architectural differences between strictly structured SQL databases requiring rigid ACID compliance, and the massive horizontal scaling capabilities of modern NoSQL document stores (like MongoDB, Cassandra, and Redis) designed to handle unstructured Big Data. His content delves into indexing strategies, query optimization, and the complexities of eventual consistency in distributed systems.</li>
<li><strong>Web3 & Decentralized Technologies:</strong> Beyond the speculative noise of cryptocurrency markets, Himanshu deeply analyzes the underlying cryptographic consensus mechanisms that power blockchain technology. He explores the potential of Smart Contracts to automate trust, the architecture of decentralized applications (dApps), and the philosophical implications of a user-owned, cryptographically secure internet layer.</li>
</ul>

<h2>4. The TyagiHub Educational Philosophy</h2>
<p><em>"Technology should not be a secret language spoken only by the corporate elite,"</em> Himanshu frequently states. <em>"When we rely on technology for our banking, our private communications, our healthcare, and our democracy, digital literacy immediately transcends from a mere skill to a fundamental human right. My ultimate goal is to ensure that anyone with a basic internet connection and a genuine willingness to read can understand exactly how their digital world is being engineered."</em></p>
<p>This strict, unyielding philosophy dictates the signature TyagiHub format: absolutely no clickbait titles, no superficial 300-word summaries, and absolutely no corporate jargon utilized without a clear, plain-English definition provided immediately. Every single guide authored by Himanshu is a comprehensive deep dive designed to build genuine, foundational comprehension rather than just rote memorization for a university exam.</p>
<p>He believes that the best way to learn complex systems is through analogical reasoning—connecting abstract, invisible digital processes to tangible, real-world examples. Whether comparing a CPU to a master chef in a busy kitchen, or likening a cloud server to a rented pizza oven, Himanshu’s writing is celebrated for its clarity, accessibility, and engaging narrative structure.</p>

<h2>5. Beyond the Code: Open Source and Digital Privacy</h2>
<p>When he is not analyzing the latest Web3 decentralized whitepaper, drafting a highly complex 3,000-word tutorial on Operating System kernel panics, or debugging a faulty backend server architecture, Himanshu is a vocal and fierce advocate for the Open-Source Software (OSS) movement and global digital privacy rights.</p>
<p>He fundamentally believes that the future of the internet must remain decentralized, secure, and user-centric. In an era where surveillance capitalism and algorithmic manipulation run rampant, he actively promotes tools, browsers, and frameworks that prioritize user autonomy and do not harvest personal data for profit. He believes that the code running our society should be open for public auditing, ensuring that algorithmic bias and unethical data harvesting are dragged into the light and permanently eradicated.</p>
<p>Himanshu frequently contributes to open-source discussions, encouraging young developers to read community code, submit pull requests, and participate in the collaborative global effort that drives true innovation. He argues that the open-source community is the most powerful educational resource available to modern programmers, providing unparalleled access to the minds of the world's greatest software engineers.</p>

<h2>6. Industry Vision & The Decade Ahead</h2>
<p>Looking toward the future, Himanshu is deeply analytical about the trajectory of emerging technologies. He predicts that the next decade will be defined by the convergence of several major technological vectors: the rollout of ultra-low-latency 6G networks, the maturation of Quantum Computing to solve complex cryptographic and molecular modeling problems, and the ubiquitous integration of Edge Computing devices in everyday environments.</p>
<p>He cautions, however, that with this immense power comes a profound ethical responsibility. As Artificial Intelligence approaches generalized capabilities, the tech community must prioritize safety, transparency, and human-centric design. Himanshu uses TyagiHub as a platform to not only explain *how* these technologies work, but to foster critical discussions about *why* we are building them and *who* ultimately benefits from their deployment.</p>

<h2>7. A Personal Message to the Readers</h2>
<p><em>"If you are reading this, I want to personally thank you for visiting TyagiHub. Building this platform has been the most rewarding engineering and educational challenge of my life. I know that computer science can seem impossibly daunting when you first look at a terminal window, a complex database schema, or a dense block of algorithmic code. But I promise you: it is not magic. It is just logic, layered meticulously on top of more logic. </em></p>
<p><em>If you take the time to peel back those layers one by one, to ask questions, and to refuse to be intimidated by technical jargon, you will realize that you possess the power to build incredible things. The digital world is malleable; it is waiting for your ideas, your code, and your vision. Keep reading, keep breaking things in safe environments, and never let a temporary bug stop you from a lifetime of learning. The future belongs to those who understand the machinery that drives it."</em> - Himanshu Tyagi</p>

<div style="text-align: center; margin-top: 60px; padding-bottom: 30px;">
    <a href="contact.html" style="display: inline-block; padding: 18px 45px; background: var(--primary-color); color: #fff; border-radius: 10px; text-decoration: none; font-weight: 800; font-size: 1.35rem; transition: background 0.3s ease, transform 0.2s ease; box-shadow: 0 5px 15px rgba(37,99,235,0.3);">Get In Touch With Himanshu &rarr;</a>
</div>
"""

# Append the new massive bio
center_div.insert_after(BeautifulSoup(html_bio, 'html.parser'))

with open(author_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Updated author.html with 1500+ word biography.")
