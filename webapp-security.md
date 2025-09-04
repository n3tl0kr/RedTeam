# 🌐 Web Application Security

> **Web Vulnerability Assessment, Testing, and Exploitation** - Comprehensive resources for web application penetration testing and security research.

---

## 🎯 Overview

This page contains essential tools, techniques, and resources for web application security testing. From OWASP Top 10 vulnerabilities to advanced exploitation techniques, discover the methodologies used by web security professionals.

---

## 🚨 OWASP Top 10 (2021)

### **A01:2021 - Broken Access Control**
- **Description**: Restrictions on what authenticated users are allowed to do
- **Tools**: Burp Suite, OWASP ZAP, custom access control testing scripts
- **Resources**: [OWASP Access Control Guide](https://owasp.org/www-project-proactive-controls/v3/en/c7-enforce-access-controls)

### **A02:2021 - Cryptographic Failures**
- **Description**: Failures related to cryptography which often lead to exposure of sensitive data
- **Tools**: SSL Labs, TestSSL.sh, custom crypto analysis scripts
- **Resources**: [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

### **A03:2021 - Injection**
- **Description**: SQL, NoSQL, OS, and LDAP injection vulnerabilities
- **Tools**: SQLMap, NoSQLMap, custom injection payloads
- **Resources**: [OWASP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)

### **A04:2021 - Insecure Design**
- **Description**: Flaws in design and architecture that cannot be fixed by proper implementation
- **Tools**: Threat modeling tools, architecture review frameworks
- **Resources**: [OWASP Secure Design Principles](https://owasp.org/www-project-proactive-controls/v3/en/c1-define-security-requirements)

### **A05:2021 - Security Misconfiguration**
- **Description**: Incorrectly configured permissions, default accounts, error handling
- **Tools**: Nikto, custom configuration scanners, manual review
- **Resources**: [OWASP Configuration Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Configuration_Cheat_Sheet.html)

### **A06:2021 - Vulnerable and Outdated Components**
- **Description**: Known vulnerabilities in components and dependencies
- **Tools**: OWASP Dependency Check, Snyk, custom dependency scanners
- **Resources**: [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)

### **A07:2021 - Identification and Authentication Failures**
- **Description**: Weaknesses in authentication mechanisms
- **Tools**: Custom authentication testing scripts, credential stuffing tools
- **Resources**: [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

### **A08:2021 - Software and Data Integrity Failures**
- **Description**: Integrity failures in software updates, CI/CD pipelines, and data
- **Tools**: Integrity checking tools, CI/CD security scanners
- **Resources**: [OWASP Software Supply Chain Security](https://owasp.org/www-project-software-supply-chain-security/)

### **A09:2021 - Security Logging and Monitoring Failures**
- **Description**: Insufficient logging, monitoring, and incident response
- **Tools**: Log analysis tools, SIEM platforms, custom monitoring scripts
- **Resources**: [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

### **A10:2021 - Server-Side Request Forgery (SSRF)**
- **Description**: Forcing the server to make requests to unintended locations
- **Tools**: Custom SSRF payloads, Burp Suite Collaborator
- **Resources**: [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)

---

## 🛠️ Web Application Scanners

### **Automated Scanners**
- **[OWASP ZAP](https://owasp.org/www-project-zap/)** - Free web application security scanner
- **[Burp Suite](https://portswigger.net/burp)** - Professional web application security testing platform
- **[Arachni](https://www.arachni-scanner.com/)** - Web application security scanner framework
- **[Skipfish](https://github.com/spinkham/skipfish)** - Web application security scanner
- **[W3AF](https://github.com/andresriancho/w3af)** - Web application attack and audit framework

### **Specialized Scanners**
- **[WPScan](https://wpscan.com/)** - WordPress security scanner
- **[JoomScan](https://github.com/OWASP/joomscan)** - Joomla vulnerability scanner
- **[Droopescan](https://github.com/droope/droopescan)** - Drupal security scanner
- **[CMSmap](https://github.com/Dionach/CMSmap)** - CMS vulnerability scanner
- **[VulnHub](https://www.vulnhub.com/)** - Vulnerable web applications for practice

---

## 🔍 Manual Testing Tools

### **Proxy & Interception**
- **[Burp Suite](https://portswigger.net/burp)** - Professional web application security testing
- **[OWASP ZAP](https://owasp.org/www-project-zap/)** - Free alternative to Burp Suite
- **[Fiddler](https://www.telerik.com/fiddler)** - Web debugging proxy
- **[Charles Proxy](https://www.charlesproxy.com/)** - Web debugging proxy for macOS
- **[mitmproxy](https://mitmproxy.org/)** - Interactive HTTPS proxy

### **Browser Extensions**
- **[HackBar](https://addons.mozilla.org/en-US/firefox/addon/hackbar/)** - Security testing toolbar
- **[Web Developer](https://addons.mozilla.org/en-US/firefox/addon/web-developer/)** - Web development tools
- **[Cookie Editor](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)** - Cookie management
- **[Wappalyzer](https://www.wappalyzer.com/)** - Technology detection
- **[BuiltWith](https://builtwith.com/)** - Technology profiler

---

## 💉 Injection Testing

### **SQL Injection**
- **[SQLMap](https://github.com/sqlmapproject/sqlmap)** - Automatic SQL injection and database takeover
- **[SQLNinja](https://github.com/xxgrunge/sqlninja)** - SQL Server injection and takeover
- **[Havij](https://github.com/)** - Automated SQL injection tool
- **[Pangolin](https://github.com/)** - SQL injection testing tool
- **Custom Payloads**: Boolean-based, time-based, error-based, union-based

### **NoSQL Injection**
- **[NoSQLMap](https://github.com/codingo/NoSQLMap)** - Automated NoSQL database enumeration and web application exploitation
- **Custom Payloads**: MongoDB, CouchDB, Redis injection techniques
- **Testing Methods**: Boolean-based, JavaScript injection, array injection

### **Command Injection**
- **[Commix](https://github.com/commixproject/commix)** - Automated command injection tool
- **Custom Payloads**: OS command injection, blind command injection
- **Testing Methods**: Time-based, output-based, blind techniques

---

## 🔐 Authentication & Session Testing

### **Authentication Testing**
- **[Hydra](https://github.com/vanhauser-thc/thc-hydra)** - Password brute-forcing
- **[Medusa](https://github.com/jmk-foofus/medusa)** - Parallel login brute-forcing
- **[Patator](https://github.com/lanjelot/patator)** - Multi-purpose brute-forcing
- **Custom Scripts**: Authentication bypass, weak password policies
- **Testing Methods**: Credential stuffing, weak authentication

### **Session Management**
- **[Burp Suite Session Handling](https://portswigger.net/burp/documentation/desktop/tools/session-handling-rules)** - Session management testing
- **Custom Scripts**: Session fixation, session hijacking
- **Testing Methods**: Session timeout, concurrent sessions, session invalidation

---

## 🌐 API Security Testing

### **API Discovery & Enumeration**
- **[Burp Suite API Testing](https://portswigger.net/burp/documentation/desktop/tools/api-testing)** - API security testing
- **[Postman](https://www.postman.com/)** - API development and testing
- **[Insomnia](https://insomnia.rest/)** - API client and testing
- **Custom Scripts**: API endpoint discovery, parameter enumeration

### **API Vulnerability Testing**
- **Authentication**: API key testing, OAuth vulnerabilities
- **Authorization**: Role-based access control testing
- **Input Validation**: Parameter injection, data validation
- **Rate Limiting**: Bypass techniques, DoS testing

---

## 📱 Mobile Web Application Testing

### **Mobile Web Security**
- **[OWASP Mobile Security Testing Guide](https://owasp.org/www-project-mobile-security-testing-guide/)** - Mobile app security testing
- **[Burp Suite Mobile Testing](https://portswigger.net/burp/documentation/desktop/tools/mobile-testing)** - Mobile app testing
- **[Frida](https://frida.re/)** - Dynamic instrumentation toolkit
- **[Objection](https://github.com/sensepost/objection)** - Runtime mobile exploration

---

## 📚 Learning Resources

### **Books**
- **["The Web Application Hacker's Handbook"](https://www.wiley.com/en-us/The+Web+Application+Hacker%27s+Handbook%3A+Finding+and+Exploiting+Security+Flaws%2C+2nd+Edition-p-9781118026472)** - Dafydd Stuttard & Marcus Pinto
- **["Web Application Security"](https://www.oreilly.com/library/view/web-application-security/9781492093109/)** - Andrew Hoffman
- **["OWASP Testing Guide"](https://owasp.org/www-project-web-security-testing-guide/)** - OWASP Foundation

### **Online Courses**
- **[Web Security Academy](https://portswigger.net/web-security)** - Free web security training
- **[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)** - Vulnerable web application
- **[DVWA](https://github.com/digininja/DVWA)** - Damn Vulnerable Web Application

### **Practice Labs**
- **[HackTheBox Web Challenges](https://www.hackthebox.com/)** - Web application challenges
- **[TryHackMe Web Path](https://tryhackme.com/)** - Web security learning path
- **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** - Free web security training

---

## 🚨 Legal & Ethical Considerations

### **Authorization Requirements**
- **Written Permission** - Always obtain explicit authorization
- **Scope Definition** - Clearly define what applications can be tested
- **Time Constraints** - Respect testing windows and schedules
- **Documentation** - Keep detailed records of all activities

### **Responsible Disclosure**
- **Vendor Notification** - Report vulnerabilities to affected parties
- **Coordinated Disclosure** - Work with vendors on responsible disclosure
- **Public Disclosure** - Only disclose after patches are available
- **Proof of Concept** - Provide sufficient detail for reproduction

---

## 🔮 Advanced Techniques

### **Client-Side Security**
- **JavaScript Security** - XSS, CSRF, client-side validation bypass
- **HTML5 Security** - WebSocket vulnerabilities, postMessage security
- **Browser Security** - Same-origin policy, content security policy

### **Modern Web Technologies**
- **SPA Security** - Single page application vulnerabilities
- **WebSocket Security** - Real-time communication security
- **Progressive Web Apps** - PWA security considerations

---

## 🤝 Contributing

We welcome contributions to expand this web application security resource collection! Please:

- **Add new tools** and frameworks
- **Share custom scripts** and payloads
- **Update vulnerability databases**
- **Contribute learning resources**
- **Report broken links** or outdated information

---

## 📞 Get Involved

- **GitHub Discussions**: [RedTeam Discussions](https://github.com/n3tl0kr/RedTeam/discussions)
- **Security Community**: Join web security groups and forums
- **Bug Bounty Programs**: Practice on authorized platforms
- **CTF Competitions**: Participate in capture the flag events

---

<div align="center">
  <sub>🌐 *"The web is vast, security is essential"* 🌐</sub>
</div>
