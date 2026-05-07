/* =============================================
   script.js — Portfolio interactions
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Nav scroll effect ---------- */
  const nav = document.getElementById('nav');
  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();


  /* ---------- Mobile menu toggle ---------- */
  const toggle = document.getElementById('nav-toggle');
  const links = document.getElementById('nav-links');

  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
    toggle.classList.toggle('active');
  });

  // Close mobile menu when a link is clicked
  links.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      links.classList.remove('open');
      toggle.classList.remove('active');
    });
  });


  /* ---------- Active nav link on scroll ---------- */
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a');

  const highlightNav = () => {
    const scrollY = window.scrollY + 120;
    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      const anchor = document.querySelector(`.nav-links a[href="#${id}"]`);
      if (anchor) {
        if (scrollY >= top && scrollY < top + height) {
          navAnchors.forEach(a => a.classList.remove('active'));
          anchor.classList.add('active');
        }
      }
    });
  };
  window.addEventListener('scroll', highlightNav, { passive: true });


  /* ---------- Scroll-reveal animation ---------- */
  const revealTargets = [
    '.overview-card',
    '.insight-card',
    '.persona-card',
    '.structure-item',
    '.process-step',
    '.gallery-item',
    '.prototype-callout',
    '.contribution-block',
    '.reflection-block',
    '.section-number',
    '.section-title',
    '.section-lead',
  ];

  const elements = document.querySelectorAll(revealTargets.join(', '));
  elements.forEach(el => el.classList.add('reveal'));

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Stagger children within the same section
        const parent = entry.target.closest('.section-inner');
        if (parent) {
          const siblings = Array.from(parent.querySelectorAll('.reveal'));
          const index = siblings.indexOf(entry.target);
          const delay = Math.min(index * 60, 300);
          entry.target.style.transitionDelay = `${delay}ms`;
        }
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -60px 0px'
  });

  elements.forEach(el => observer.observe(el));

});
