import re

with open('/Users/celinekeles/personalportfoio_celinekeles/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We will completely replace the .audience-split div to clean up the organization.
start_str = '<div class="audience-split">'
end_str = '<p class="audience-unique">'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_html = '''<div class="audience-split">
              <div class="audience-participants">
                <h4 class="audience-section-title">Participants</h4>
                <div class="persona-grid">
                  
                  <!-- Participant 1: Basic Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--3">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">Participant 1</h4>
                      <span class="persona-flow persona-flow--basic">Basic Flow</span>
                    </div>
                    <p class="persona-desc">55 years old female, not retired yet, Sonographer at Regional Hospital.</p>
                    <ul class="persona-traits">
                      <li>Needs more guidance for reading finances</li>
                      <li>Wants more simplified views and insights</li>
                      <li>Values reassurance over raw data</li>
                    </ul>
                  </div>

                  <!-- Participant 2: Advanced Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--1">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">Participant 2</h4>
                      <span class="persona-flow persona-flow--advanced">Advanced Flow</span>
                    </div>
                    <p class="persona-desc">70 year old male, retired but used to work as a SWE at an investment firm.</p>
                    <ul class="persona-traits">
                      <li>Prefers visual data (charts &amp; graphs)</li>
                      <li>Wants context, not just raw figures</li>
                      <li>Compares year-over-year performance</li>
                    </ul>
                  </div>

                  <!-- Participant 3: Basic Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--4">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">Participant 3</h4>
                      <span class="persona-flow persona-flow--basic">Basic Flow</span>
                    </div>
                    <p class="persona-desc">68 year old female, recently retired teacher. Relies on a financial advisor for most major decisions.</p>
                    <ul class="persona-traits">
                      <li>Low financial literacy</li>
                      <li>Easily overwhelmed by too much data</li>
                      <li>Wants a clear yes/no on retirement readiness</li>
                    </ul>
                  </div>

                  <!-- Participant 4: Advanced Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--2">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">Participant 4</h4>
                      <span class="persona-flow persona-flow--advanced">Advanced Flow</span>
                    </div>
                    <p class="persona-desc">62 year old male, small business owner nearing retirement. Actively tracks market trends.</p>
                    <ul class="persona-traits">
                      <li>Wants specific numbers &amp; percentages</li>
                      <li>Comfortable with financial jargon</li>
                      <li>Reads every line of their statements</li>
                    </ul>
                  </div>

                </div>
              </div>

              <div class="audience-personas">
                <h4 class="audience-section-title">Personas</h4>
                <div class="persona-grid">
                  
                  <!-- Persona 1: Basic Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--3">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">The Simplicity Seeker</h4>
                      <span class="persona-flow persona-flow--basic">Basic Flow</span>
                    </div>
                    <p class="persona-desc">A working professional who doesn't have the time or desire to learn financial jargon. They check their account occasionally and want a friendly, digestible summary that reassures them without requiring deep analysis.</p>
                    <ul class="persona-traits">
                      <li>Advisor-dependent, checks in periodically</li>
                      <li>Prefers plain-language explanations</li>
                      <li>Needs simple, clear insights</li>
                    </ul>
                  </div>

                  <!-- Persona 2: Advanced Flow (User's custom text) -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--1">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">The Analytical Expert</h4>
                      <span class="persona-flow persona-flow--advanced">Advanced Flow</span>
                    </div>
                    <p class="persona-desc">A semi-retired professional who tracks market trends. Very serious about his retirement plan. Since his early 20s, he has focused on staying ahead in savings and investment. He appreciates charts but wants the Year in Review to contextualize data.</p>
                    <ul class="persona-traits">
                      <li>Wants detailed numerical breakdowns</li>
                      <li>Financially educated &amp; data-driven</li>
                      <li>Comfortable interpreting charts &amp; metrics</li>
                    </ul>
                  </div>

                  <!-- Persona 3: Basic Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--4">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">The Anxious Retiree</h4>
                      <span class="persona-flow persona-flow--basic">Basic Flow</span>
                    </div>
                    <p class="persona-desc">Recently retired and new to reviewing investment summaries on their own. They feel overwhelmed by financial terminology and just want to know: <em>am I on track?</em> Simplicity is everything.</p>
                    <ul class="persona-traits">
                      <li>Easily overwhelmed by too much data</li>
                      <li>Wants a clear yes/no on readiness</li>
                      <li>Avoids complex tables</li>
                    </ul>
                  </div>

                  <!-- Persona 4: Advanced Flow -->
                  <div class="persona-card">
                    <div class="persona-avatar persona-avatar--2">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>
                    </div>
                    <div class="persona-info">
                      <h4 class="persona-name">The Hands-on Planner</h4>
                      <span class="persona-flow persona-flow--advanced">Advanced Flow</span>
                    </div>
                    <p class="persona-desc">Nearing retirement and actively managing their portfolio transition. They want granular, numerical data — returns by asset class, benchmark comparisons, and fee breakdowns.</p>
                    <ul class="persona-traits">
                      <li>Compares year-over-year performance</li>
                      <li>Wants context for market shifts</li>
                      <li>Analyzes asset allocation</li>
                    </ul>
                  </div>

                </div>
              </div>
            </div>

            '''
    
    new_content = content[:start_idx] + new_html + content[end_idx:]
    with open('/Users/celinekeles/personalportfoio_celinekeles/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: HTML updated.")
else:
    print("ERROR: Could not find target strings.")
