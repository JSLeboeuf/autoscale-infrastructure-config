#!/usr/bin/env python3
"""Test Namecheap API connection - Template version using environment variables"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import os
import sys

# Load credentials from environment variables
API_USER = os.getenv("NAMECHEAP_API_USER")
API_KEY = os.getenv("NAMECHEAP_API_KEY")
USERNAME = os.getenv("NAMECHEAP_USERNAME")
CLIENT_IP = os.getenv("NAMECHEAP_CLIENT_IP")

def test_namecheap_connection():
    """Test connection to Namecheap API by getting domain list"""

    # Check if credentials are set
    if not all([API_USER, API_KEY, USERNAME, CLIENT_IP]):
        print("❌ Error: Missing environment variables")
        print("   Required: NAMECHEAP_API_USER, NAMECHEAP_API_KEY, NAMECHEAP_USERNAME, NAMECHEAP_CLIENT_IP")
        print()
        print("   Set them with:")
        print("   export NAMECHEAP_API_USER=your_username")
        print("   export NAMECHEAP_API_KEY=your_api_key")
        print("   export NAMECHEAP_USERNAME=your_username")
        print("   export NAMECHEAP_CLIENT_IP=your_whitelisted_ip")
        print()
        print("   Or source your .env file:")
        print("   set -a && source .env && set +a")
        return False

    print("🔍 Testing Namecheap API Connection...")
    print(f"   API User: {API_USER}")
    print(f"   Client IP: {CLIENT_IP}")
    print()

    # API endpoint
    base_url = "https://api.namecheap.com/xml.response"

    # Parameters
    params = {
        "ApiUser": API_USER,
        "ApiKey": API_KEY,
        "UserName": USERNAME,
        "ClientIp": CLIENT_IP,
        "Command": "namecheap.domains.getList",
        "PageSize": "100",
        "Page": "1"
    }

    # Build URL
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        # Make request
        print("📡 Sending request to Namecheap API...")
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()

        # Parse XML response
        root = ET.fromstring(data)

        # Check for errors
        errors = root.findall(".//{http://api.namecheap.com/xml.response}Errors/{http://api.namecheap.com/xml.response}Error")

        if errors:
            print("❌ API Error:")
            for error in errors:
                print(f"   {error.text}")
            return False

        # Get domains
        domains = root.findall(".//{http://api.namecheap.com/xml.response}Domain")

        print(f"✅ Connection successful!")
        print(f"\n📋 Found {len(domains)} domain(s):")

        for domain in domains:
            name = domain.get("Name", "Unknown")
            expires = domain.get("Expires", "Unknown")
            auto_renew = domain.get("AutoRenew", "Unknown")
            is_locked = domain.get("IsLocked", "Unknown")

            print(f"\n   🌐 Domain: {name}")
            print(f"      Expires: {expires}")
            print(f"      Auto-Renew: {auto_renew}")
            print(f"      Locked: {is_locked}")

        return True

    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        print(f"   Response: {e.read().decode()}")
        return False

    except urllib.error.URLError as e:
        print(f"❌ URL Error: {e.reason}")
        return False

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("\n" + "="*60)
    print("   NAMECHEAP API CONNECTION TEST")
    print("="*60 + "\n")

    success = test_namecheap_connection()

    print("\n" + "="*60)
    if success:
        print("   ✅ NAMECHEAP: OPERATIONAL")
    else:
        print("   ❌ NAMECHEAP: FAILED")
    print("="*60 + "\n")

    sys.exit(0 if success else 1)
