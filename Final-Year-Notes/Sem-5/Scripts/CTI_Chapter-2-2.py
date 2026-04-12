import os

glossary_path = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Notes/Glossary"

definitions = {
    "Threat Actors": "# Threat Actors\n**Threat Actors** are individuals or groups who perform malicious acts against an organization. They are categorized by motivation and capability.\n*   **Types**: Nation-States, Cybercriminals, Hacktivists, Insider Threats.",
    "Indicators": "# Indicators\n**Indicators** (or Indicators of Compromise - [[IoC]]) are technical artifacts that suggest an attack is happening or has happened.\n*   **Examples**: IP addresses, File Hashes, Domain names.",
    "TTPs": "# TTPs\n**TTPs** stands for **Tactics, Techniques, and Procedures**. It describes *how* threat actors operate.\n*   **Tactics**: The \"Why\" (Goal).\n*   **Techniques**: The \"How\" (Method).\n*   **Procedures**: The specific steps.",
    "IoC": "# IoC\n**IoC** (Indicator of Compromise) is a piece of forensic data that identifies potentially malicious activity on a system or network.\n*   **Use**: Reactive detection (finding what has already happened).",
    "IoA": "# IoA\n**IoA** (Indicator of Attack) focuses on detecting the intent of an attacker and the steps they are taking, often before the compromise is complete.\n*   **Use**: Proactive detection.",
    "CTI": "# CTI\n**CTI** (Cyber Threat Intelligence) is analyzed information about the hostile intent, capability, and opportunity of an adversary.",
    "Cyber Kill Chain": "# Cyber Kill Chain\nThe **Cyber Kill Chain**, developed by Lockheed Martin, is a framework that identifies the stages of a cyber attack.\n1.  Reconnaissance\n2.  Weaponization\n3.  Delivery\n4.  Exploitation\n5.  Installation\n6.  Command and Control (C2)\n7.  Actions on Objectives",
    "Pyramid of Pain": "# Pyramid of Pain\nThe **Pyramid of Pain** illustrates the relationship between the types of indicators you use to detect an adversary and how much pain it causes them when you deny those indicators.\n*   **Levels (Low to High Pain)**: Hash Values -> IP Addresses -> Domain Names -> Network/Host Artifacts -> Tools -> [[TTPs]].",
    "Security Alerts": "# Security Alerts\n**Security Alerts** are human-readable notifications, such as advisories or bulletins, that warn of specific threats or vulnerabilities.",
    "Threat Intelligence Reports": "# Threat Intelligence Reports\n**Threat Intelligence Reports** are detailed documents (often prose) that describe threat actors, their campaigns, and their TTPs.",
    "Traffic Light Protocol": "# Traffic Light Protocol\n**Traffic Light Protocol (TLP)** is a set of designations used to ensure that sensitive information is shared with the appropriate audience.\n*   **Red**: Personal/Restricted.\n*   **Amber**: Limited Distribution.\n*   **Green**: Community Wide.\n*   **White**: Unlimited/Public.",
    "TLP": "# TLP\nSee [[Traffic Light Protocol]].",
    "Cybercrime": "# Cybercrime\n**Cybercrime** refers to criminal activities carried out using computers or the internet. It includes fraud, identity theft, and cyberstalking.",
    "Cyberwar": "# Cyberwar\n**Cyberwar** involves the use of digital attacks by one nation-state to disrupt the vital computer systems of another, often with the aim of creating damage, death, or destruction.",
    "Ransomware": "# Ransomware\n**Ransomware** is a type of malware that threatens to publish the victim's data or perpetually block access to it unless a ransom is paid.",
    "Spear Phishing": "# Spear Phishing\n**Spear Phishing** is a targeted attempt to steal sensitive information such as account credentials or financial information from a specific victim, often for malicious reasons.",
    "Phishing": "# Phishing\n**Phishing** is a type of social engineering where an attacker sends a fraudulent message designed to trick a human victim into revealing sensitive information.",
    "Backdoors": "# Backdoors\nA **Backdoor** is a method of bypassing normal authentication or encryption in a computer system, a product, or an embedded device, etc.",
    "Evasion Techniques": "# Evasion Techniques\n**Evasion Techniques** are methods used by malware or attackers to avoid detection by security solutions (like Antivirus or IDS).",
    "Sony Hack": "# Sony Hack\nThe **Sony Hack** (2014) was a major cyberattack against Sony Pictures, attributed to North Korea (Lazarus Group), involving the release of confidential data and destruction of systems.",
    "Stuxnet": "# Stuxnet\n**Stuxnet** is a malicious computer worm, first uncovered in 2010, that targets SCADA systems and is believed to be responsible for causing substantial damage to Iran's nuclear program.",
    "Internet of Things": "# Internet of Things\nThe **Internet of Things (IoT)** describes the network of physical objects—\"things\"—that are embedded with sensors, software, and other technologies for the purpose of connecting and exchanging data with other devices and systems over the internet.",
    "Big Data": "# Big Data\n**Big Data** refers to data sets that are too large or complex to be dealt with by traditional data-processing application software.",
    "Cryptocurrency": "# Cryptocurrency\nA **Cryptocurrency** is a digital currency in which transactions are verified and records maintained by a decentralized system using cryptography, rather than by a centralized authority.",
    "Deep Web": "# Deep Web\nThe **Deep Web** is the part of the World Wide Web whose contents are not indexed by standard web search-engines (e.g., banking sites, private databases).",
    "Dark Web": "# Dark Web\nThe **Dark Web** is a part of the internet that isn't indexed by search engines and requires specific software, configurations, or authorization to access (e.g., Tor).",
    "Firewall": "# Firewall\nA **Firewall** is a network security device that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies.",
    "VPN": "# VPN\nA **VPN (Virtual Private Network)** extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network.",
    "Syslog": "# Syslog\n**Syslog** is a standard for message logging. It allows separation of the software that generates messages, the system that stores them, and the software that reports and analyzes them.",
    "NetFlow": "# NetFlow\n**NetFlow** is a network protocol developed by Cisco for collecting IP traffic information and monitoring network traffic.",
    "MFA": "# MFA\n**MFA (Multi-Factor Authentication)** is an authentication method in which a computer user is granted access only after successfully presenting two or more pieces of evidence (or factors) to an authentication mechanism.",
    "RBAC": "# RBAC\n**RBAC (Role-Based Access Control)** is a method of restricting network access based on the roles of individual users within an enterprise.",
    "STIX": "# STIX\n**STIX (Structured Threat Information Expression)** is a standardized language for representing and sharing cyber threat information.",
    "TAXII": "# TAXII\n**TAXII (Trusted Automated Exchange of Intelligence Information)** is an application layer protocol for the communication of cyber threat information in a simple and scalable manner.",
    "CybOX": "# CybOX\n**CybOX (Cyber Observable Expression)** is a standardized schema for specifying, capturing, characterizing, and communicating events or stateful properties that are observable in the operational cyber domain.",
    "IODEF": "# IODEF\n**IODEF (Incident Object Description Exchange Format)** is a data format for describing computer security information for the purpose of exchange between CSIRTs.",
    "RID": "# RID\n**RID (Real-time Inter-network Defense)** is a standard for communicating incident handling data.",
    "OpenIOC": "# OpenIOC\n**OpenIOC** is an open framework for sharing threat intelligence, specifically Indicators of Compromise.",
    "SPF": "# SPF\n**SPF (Sender Policy Framework)** is an email authentication method designed to detect forging sender addresses during the delivery of the email.",
    "DKIM": "# DKIM\n**DKIM (DomainKeys Identified Mail)** is an email authentication method that provides a mechanism to verify that an email message was not altered in transit.",
    "DMARC": "# DMARC\n**DMARC (Domain-based Message Authentication, Reporting, and Conformance)** is an email authentication protocol that uses SPF and DKIM to determine the authenticity of an email message.",
    "CVE": "# CVE\n**CVE (Common Vulnerabilities and Exposures)** is a list of publicly disclosed computer security flaws.",
    "CPE": "# CPE\n**CPE (Common Platform Enumeration)** is a structured naming scheme for information technology systems, software, and packages.",
    "CWE": "# CWE\n**CWE (Common Weakness Enumeration)** is a community-developed list of common software and hardware weakness types.",
    "NIS Directive": "# NIS Directive\nThe **NIS Directive** is the first piece of EU-wide legislation on cybersecurity, providing legal measures to boost the overall level of cybersecurity in the EU.",
    "GDPR": "# GDPR\nThe **GDPR (General Data Protection Regulation)** is a regulation in EU law on data protection and privacy in the European Union and the European Economic Area.",
    "CISA": "# CISA\n**CISA (Cybersecurity and Infrastructure Security Agency)** is a standalone United States federal agency, an operational component under the Department of Homeland Security oversight.",
    "ENISA": "# ENISA\n**ENISA** is the European Union Agency for Cybersecurity.",
    "NIST": "# NIST\n**NIST (National Institute of Standards and Technology)** is a physical sciences laboratory and a non-regulatory agency of the United States Department of Commerce.",
    "FIRST": "# FIRST\n**FIRST (Forum of Incident Response and Security Teams)** is a global non-profit organization dedicated to bringing together incident response teams.",
    "APCERT": "# APCERT\n**APCERT (Asia Pacific Computer Emergency Response Team)** is a coalition of CSIRTs from the Asia Pacific region.",
    "CERT": "# CERT\n**CERT (Computer Emergency Response Team)** is an expert group that handles computer security incidents.",
    "CSIRT": "# CSIRT\n**CSIRT (Computer Security Incident Response Team)** is a concrete organizational entity (i.e., one or more staff) that is assigned the responsibility for coordinating and supporting the response to a computer security event or incident.",
    "NDN": "# NDN\n**NDN (National Detection Network)** is a Dutch network for sharing threat information.",
    "ETIS": "# ETIS\n**ETIS** is a non-profit organization which brings together the major telecommunications providers in Europe to share knowledge on key industry issues.",
    "MISP": "# MISP\n**MISP (Malware Information Sharing Platform)** is an open source software solution for collecting, storing, distributing and sharing cyber security indicators and threats.",
    "Ontology": "# Ontology\nIn computer science, an **Ontology** is a representation, formal naming and definition of the categories, properties and relations between the concepts, data and entities that substantiate one, many or all domains of discourse.",
    "Threat Intelligence Cycle": "# Threat Intelligence Cycle\nThe **Threat Intelligence Cycle** is the process of transforming raw data into actionable intelligence. Steps: Planning, Collection, Processing, Analysis, Dissemination, Feedback."
}

if not os.path.exists(glossary_path):
    os.makedirs(glossary_path)

for filename, content in definitions.items():
    file_path = os.path.join(glossary_path, f"{filename}.md")
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created {file_path}")
