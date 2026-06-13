import random

svg = []
svg.append('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="250" viewBox="0 0 800 250">')
svg.append('  <defs>')
svg.append('    <linearGradient id="skyGradient" x1="0%" y1="0%" x2="100%" y2="100%">')
svg.append('      <stop offset="0%" stop-color="#0d041c" />')
svg.append('      <stop offset="50%" stop-color="#180a30" />')
svg.append('      <stop offset="100%" stop-color="#05010f" />')
svg.append('    </linearGradient>')
svg.append('    <style>')
svg.append('      .star { fill: #ffffff; animation: twinkle ease-in-out infinite alternate; }')
svg.append('      @keyframes twinkle { 0% { opacity: 0.1; r: 0.5px; } 100% { opacity: 1; r: 2px; } }')
svg.append('      .shooting-star { fill: none; stroke: #ffffff; stroke-width: 1.5; stroke-dasharray: 150; stroke-dashoffset: 150; animation: shoot linear infinite; opacity: 0; }')
svg.append('      @keyframes shoot { 0% { stroke-dashoffset: 150; opacity: 1; } 10% { stroke-dashoffset: 0; opacity: 0; } 100% { stroke-dashoffset: 0; opacity: 0; } }')
svg.append('    </style>')
svg.append('  </defs>')
svg.append('  <rect width="100%" height="100%" fill="url(#skyGradient)" />')

for _ in range(250):
    cx = random.uniform(0, 800)
    cy = random.uniform(0, 250)
    delay = random.uniform(0, 5)
    duration = random.uniform(1.5, 4)
    r_base = random.uniform(0.5, 1.5)
    svg.append(f'  <circle class="star" cx="{cx:.2f}" cy="{cy:.2f}" r="{r_base:.2f}" style="animation-duration: {duration:.2f}s; animation-delay: {delay:.2f}s;" />')

for i in range(4):
    start_x = random.uniform(200, 800)
    start_y = random.uniform(0, 100)
    end_x = start_x - 200
    end_y = start_y + 200
    delay = random.uniform(1, 10)
    svg.append(f'  <line class="shooting-star" x1="{start_x:.2f}" y1="{start_y:.2f}" x2="{end_x:.2f}" y2="{end_y:.2f}" style="animation-duration: 8s; animation-delay: {delay:.2f}s;" />')

svg.append('</svg>')

with open('assets/galaxy.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))
print('SVG Galaxy Generated!')
