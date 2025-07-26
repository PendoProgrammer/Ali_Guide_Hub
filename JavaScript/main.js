 document.addEventListener("DOMContentLoaded", function () {

      // Mobile Menu Toggle
      const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
      const navLinks = document.querySelector(".nav-links");

      mobileMenuBtn.addEventListener("click", () => {
        navLinks.classList.toggle("active");
        mobileMenuBtn.innerHTML = navLinks.classList.contains("active")
          ? '<i class="fas fa-times"></i>'
          : '<i class="fas fa-bars"></i>';
      });

      // Close mobile menu when clicking a link
      document.querySelectorAll(".nav-links a").forEach((link) => {
        link.addEventListener("click", () => {
          navLinks.classList.remove("active");
          mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
        });
      });

      // Scroll to Top Button
      const scrollTopBtn = document.querySelector(".scroll-top");

      window.addEventListener("scroll", () => {
        if (window.pageYOffset > 300) {
          scrollTopBtn.classList.add("active");
        } else {
          scrollTopBtn.classList.remove("active");
        }
      });

      scrollTopBtn.addEventListener("click", () => {
        window.scrollTo({
          top: 0,
          behavior: "smooth",
        });
      });

      // Lazy Loading for Images
      document.addEventListener("DOMContentLoaded", function () {
        const lazyImages = [].slice.call(
          document.querySelectorAll('img[loading="lazy"]')
        );

        if ("IntersectionObserver" in window) {
          const lazyImageObserver = new IntersectionObserver(function (
            entries,
            observer
          ) {
            entries.forEach(function (entry) {
              if (entry.isIntersecting) {
                const lazyImage = entry.target;
                lazyImage.src = lazyImage.src;
                lazyImageObserver.unobserve(lazyImage);
              }
            });
          });

          lazyImages.forEach(function (lazyImage) {
            lazyImageObserver.observe(lazyImage);
          });
        }
      });

      // Smooth Scrolling for Anchor Links
      document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", function (e) {
          e.preventDefault();

          const targetId = this.getAttribute("href");
          if (targetId === "#") return;

          const targetElement = document.querySelector(targetId);
          if (targetElement) {
            targetElement.scrollIntoView({
              behavior: "smooth",
            });

            // Close mobile menu if open
            if (navLinks.classList.contains("active")) {
              navLinks.classList.remove("active");
              mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
          }
        });
      });

      // Newsletter Form Submission
      const newsletterForm = document.querySelector(".newsletter-form");

      if (newsletterForm) {
        newsletterForm.addEventListener("submit", function (e) {
          e.preventDefault();
          const emailInput = this.querySelector('input[type="email"]');
          const email = emailInput.value;

          // Simple validation
          if (!email || !email.includes("@")) {
            alert("Please enter a valid email address");
            return;
          }

          // Here you would typically send the email to your server
          console.log("Subscribed email:", email);

          // Show success message
          alert("Thank you for subscribing to our newsletter!");
          emailInput.value = "";
        });
      }

      // Contact Form Submission (example for contact page)
      const contactForm = document.querySelector(".contact-form form");

      if (contactForm) {
        contactForm.addEventListener("submit", function (e) {
          e.preventDefault();

          // Get form values
          const name = this.querySelector('input[name="name"]').value;
          const email = this.querySelector('input[name="email"]').value;
          const subject = this.querySelector('input[name="subject"]').value;
          const message = this.querySelector('textarea[name="message"]').value;

          // Simple validation
          if (!name || !email || !subject || !message) {
            alert("Please fill in all fields");
            return;
          }

          if (!email.includes("@")) {
            alert("Please enter a valid email address");
            return;
          }

          // Here you would typically send this data to your server
          console.log("Contact form submitted:", {
            name,
            email,
            subject,
            message,
          });

          // Show success message
          alert("Thank you for your message! We will get back to you soon.");
          this.reset();
        });
      }

      // Comment Form Submission (example for blog post page)
      const commentForm = document.querySelector(".comment-form");

      if (commentForm) {
        commentForm.addEventListener("submit", function (e) {
          e.preventDefault();

          // Get form values
          const name = this.querySelector('input[name="name"]').value;
          const email = this.querySelector('input[name="email"]').value;
          const comment = this.querySelector('textarea[name="comment"]').value;

          // Simple validation
          if (!name || !email || !comment) {
            alert("Please fill in all fields");
            return;
          }

          if (!email.includes("@")) {
            alert("Please enter a valid email address");
            return;
          }

          // Create new comment element
          const commentsList = document.querySelector(".comments-list");
          const newComment = document.createElement("div");
          newComment.className = "comment";
          newComment.innerHTML = `
                    <div class="comment-avatar">${name
                      .charAt(0)
                      .toUpperCase()}</div>
                    <div class="comment-content">
                        <h4>${name} <span class="badge badge-primary">New</span></h4>
                        <div class="comment-meta">Just now</div>
                        <p class="comment-text">${comment}</p>
                        <a href="#" class="reply-btn"><i class="fas fa-reply"></i> Reply</a>
                    </div>
                `;

          // Add new comment to the top of the list
          commentsList.insertBefore(newComment, commentsList.firstChild);

          // Reset form
          this.reset();

          // Show success message
          alert("Thank you for your comment!");
        });
      }

      // Animation on scroll
      const animateOnScroll = function () {
        const elements = document.querySelectorAll(".fade-in");

        elements.forEach((element) => {
          const elementPosition = element.getBoundingClientRect().top;
          const windowHeight = window.innerHeight;

          if (elementPosition < windowHeight - 100) {
            element.style.opacity = "1";
            element.style.transform = "translateY(0)";
          }
        });
      };

      window.addEventListener("scroll", animateOnScroll);
      window.addEventListener("load", animateOnScroll);
   
});