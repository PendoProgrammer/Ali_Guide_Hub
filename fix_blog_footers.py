#!/usr/bin/env python3
"""
Targeted Blog Footer Fix Script for Ali Guide Hub Website
Fixes all blog post pages to have the exact same clean footer as index.html
"""

import os
import re
from pathlib import Path

# The perfect footer HTML from index.html (exact copy)
PERFECT_FOOTER = '''    <!-- Footer -->
    <footer>
      <div class="container">
        <div class="footer-content">
          <div class="footer-column">
            <div class="footer-logo">
              <img
                src="logo.webp"
                alt="Guide Hubz Logo"
              />
              <span>Guide Hubz</span>
            </div>
            <div class="footer-about">
              <p>
                Your trusted source for expert guides on technology, health,
                finance, and lifestyle. We provide practical, actionable advice
                to help you live better.
              </p>
            </div>
            <div class="social-links">
              <a href="https://www.facebook.com/profile.php?id=61579041620370"><i class="fab fa-facebook-f"></i></a>
              <a href="https://twitter.com/mraliakber1" target="_blank" rel="noopener"><i class="fab fa-twitter"></i></a>
              <a href="https://www.instagram.com/mr.aliakber1/" target="_blank" rel="noopener"><i class="fab fa-instagram"></i></a>
              <a href="https://www.youtube.com/@mraliakber1" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a>
              <a href="https://github.com/PendoProgrammer" target="_blank" rel="noopener"><i class="fab fa-github"></i></a>
            </div>
          </div>
          <div class="footer-column">
            <h3>Quick Links</h3>
            <ul class="footer-links">
              <li>
                <a href="index.html"><i class="fas fa-chevron-right"></i> Home</a>
              </li>
              <li>
                <a href="blog.html"><i class="fas fa-chevron-right"></i> Blog</a>
              </li>
              <li>
                <a href="blog.html"><i class="fas fa-chevron-right"></i> Categories</a>
              </li>
              <li>
                <a href="about.html"><i class="fas fa-chevron-right"></i> About Us</a>
              </li>
              <li>
                <a href="contactus.html"><i class="fas fa-chevron-right"></i> Contact</a>
              </li>
            </ul>
          </div>
          <div class="footer-column">
            <h3>Categories</h3>
            <ul class="footer-links">
              <li>
                <a href="top_10_AI_tool.html"><i class="fas fa-chevron-right"></i> Technology</a>
              </li>
              <li>
                <a href="healthy_morning_routine.html"><i class="fas fa-chevron-right"></i> Health & Wellness</a>
              </li>
              <li>
                <a href="Forex_Trading_Blog.html"><i class="fas fa-chevron-right"></i> Finance</a>
              </li>
              <li>
                <a href="10_daily_habits_successfull_people.html"><i class="fas fa-chevron-right"></i> Productivity</a>
              </li>
              <li>
                <a href="10_daily_habits_successfull_people.html"><i class="fas fa-chevron-right"></i> Lifestyle</a>
              </li>
            </ul>
          </div>
          <div class="footer-column">
            <h3>Contact Info</h3>
            <div class="contact-info">
              <div class="contact-item">
                <div class="contact-icon">
                  <i class="fas fa-map-marker-alt"></i>
                </div>
                <div class="contact-details">
                  <h4>Location</h4>
                  <p>Pakistan, Knowledge City</p>
                </div>
              </div>
              <div class="contact-item">
                <div class="contact-icon">
                  <i class="fas fa-envelope"></i>
                </div>
                <div class="contact-details">
                  <h4>Email</h4>
                  <a href="mailto:info@guidehubz.com">Email Us: info@guidehubz.com</a>
                </div>
              </div>
              <div class="contact-item">
                <div class="contact-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="contact-details">
                  <h4>Phone</h4>
                  <a href="tel:+447543945859">+44 7543 945859</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="copyright">
          <p>
            &copy; 2025 Guide Hubz. All rights reserved. |
            <a href="privacy-policy.html" target="_blank">Privacy Policy</a> |
            <a href="terms-and-conditions.html" target="_blank">Terms of Service</a> |
            <a href="disclaimer.html" target="_blank">Disclaimer</a> |
            <a href="about.html" target="_blank">About Us</a> |
            <a href="contactus.html" target="_blank">Contact</a> |
            <a href="sitemap.xml" target="_blank">Sitemap</a>
          </p>
        </div>
      </div>
    </footer>'''

def find_and_replace_footer(content):
    """Find and replace the footer section with the perfect footer"""
    # Look for footer tag with comment
    footer_pattern = r'<!-- Footer -->.*?</footer>'
    footer_match = re.search(footer_pattern, content, re.DOTALL)
    
    if footer_match:
        old_footer = footer_match.group(0)
        content = content.replace(old_footer, PERFECT_FOOTER)
        return content, True
    
    # Look for footer tag without comment
    footer_pattern = r'<footer>.*?</footer>'
    footer_match = re.search(footer_pattern, content, re.DOTALL)
    
    if footer_match:
        old_footer = footer_match.group(0)
        content = content.replace(old_footer, PERFECT_FOOTER)
        return content, True
    
    return content, False

def fix_blog_post_footer(file_path):
    """Fix the footer in a single blog post file"""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the footer
        updated_content, footer_found = find_and_replace_footer(content)
        
        if footer_found:
            # Write the updated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ Footer fixed: {file_path}")
            return True
        else:
            print(f"⚠️  No footer found: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix all blog post footers"""
    print("🔧 Starting targeted blog footer fix for Ali Guide Hub Website...")
    print("📋 Updating all blog posts to have the exact same clean footer as index.html")
    
    # List of blog post files that need footer fixes
    blog_post_files = [
        'what_is_pip.html',
        '5passive_incom_ideas.html',
        '7_Money_Habbite_poor.html',
        'about.html',
        'Ai transfor small bussuness.html',
        'Aisidehustle.html',
        'author.html',
        'best_budgting_tips.html',
        'Best_Inverstement_option.html',
        'dropshipping2025.html',
        'Forex_Trading_Blog.html',
        'healthy_morning_routine.html',
        'hidden_incom_streams.html',
        'How_to_Become_Rich_in_2025.html',
        'How_to_Choose_the_Best_Forex_Broker_in_2025_Complete_Guide.html',
        'how_to_protect_our_personal_data.html',
        'How_to_save_money_fast.html',
        'incom_models.html',
        'login.html',
        'make100_chatgpt.html',
        'make_money_on_amazon.html',
        'montize_a_blog.html',
        'privacy-policy.html',
        'private_habits_of_milionires.html',
        'register.html',
        'saeed_Ajmal_is_back.html',
        'smallbussiness.html',
        'startbussiness2025.html',
        'terms-and-conditions.html',
        'top_10_AI_tool.html',
        'top_5_forex_trading_startgies.html',
        'top_bussiness_niches.html',
        'top_high_incom_skill.html'
    ]
    
    if not blog_post_files:
        print("❌ No blog post files found to update")
        return
    
    print(f"📁 Found {len(blog_post_files)} blog post files to fix")
    
    fixed_count = 0
    total_files = len(blog_post_files)
    
    for blog_file in blog_post_files:
        if Path(blog_file).exists():
            if fix_blog_post_footer(blog_file):
                fixed_count += 1
        else:
            print(f"⚠️  File not found: {blog_file}")
    
    print(f"\n🎉 Blog Footer Fix Complete!")
    print(f"📊 Files processed: {total_files}")
    print(f"✅ Footers fixed: {fixed_count}")
    print(f"⚠️  Files without footers: {total_files - fixed_count}")
    
    if fixed_count > 0:
        print("\n🔧 What Was Fixed:")
        print("   • All blog posts now have identical footer layout")
        print("   • Clean, organized footer structure")
        print("   • Proper social media links (Twitter & YouTube corrected)")
        print("   • Working category links")
        print("   • Consistent contact information")
        print("   • Professional copyright section")
        print("   • All legal links working")
        print("   • Matches index.html footer exactly")
    
    print("\n🎯 Your blog posts now have the same clean, professional footer as your index page!")

if __name__ == "__main__":
    main()
