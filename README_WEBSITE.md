# Progressive Photorealistic Abstraction

## Paper Website

A professional GitHub Pages website for the paper "Progressive Photorealistic Abstraction: Realism and abstraction can coexist."

## Website Structure

### Main Sections

1. **Abstract** - Overview of the research contribution
2. **Architecture** - Technical details of the two-stage approach
   - Stage I: Iterative Search-Based Planner
   - Stage II: Distilled Image-to-Video Model
3. **Applications** - Three main use cases
   - Progressive Photorealistic Abstraction (interactive exploration)
   - Semantic Image De-cluttering (content-aware removal)
   - Image Layering and Semantic Decomposition (compositing workflows)
4. **Results** - Gallery of example results
5. **Paper & Code** - Links to paper, code, and supplementary materials

## Files

- `index.html` - Main website file with all sections
- `styles.css` - Responsive styling and layout
- `_config.yml` - Jekyll/GitHub Pages configuration
- `images/` - Directory for all images and visualizations

## Setup Instructions

### Option 1: Deploy to GitHub Pages

1. Update the `_config.yml` file:
   - Replace `https://yourusername.github.io/Progressive_Photorealistic_Abstraction` with your actual URL
   - Update author information

2. Push to your GitHub repository:
   ```bash
   git add .
   git commit -m "Add paper website"
   git push
   ```

3. In your GitHub repository settings:
   - Go to Settings > Pages
   - Select "Deploy from a branch"
   - Choose the branch containing this content
   - Save

4. Access your website at `https://yourusername.github.io/Progressive_Photorealistic_Abstraction`

### Option 2: Run Locally

1. Install Jekyll:
   ```bash
   gem install jekyll bundler
   ```

2. Navigate to the project directory and run:
   ```bash
   jekyll serve
   ```

3. Open `http://localhost:4000/Progressive_Photorealistic_Abstraction` in your browser

## Adding Images

The website has placeholder sections for images. Add your images to the `images/` folder:

### Required Images

**Architecture Section:**
- `architecture_stage1.png` - Diagram of Stage I
- `architecture_stage2.png` - Diagram of Stage II
- `architecture_overview.png` - Complete system overview

**Application 1 - Progressive Abstraction:**
- `app1_example1.jpg`, `app1_example2.jpg`, `app1_example3.jpg` - Example results
- `tree_structure.png` - Abstraction tree visualization

**Application 2 - De-cluttering:**
- `declutter_before1.jpg`, `declutter_after1.jpg` - Before/after examples
- `declutter_before2.jpg`, `declutter_after2.jpg` - Additional before/after examples

**Application 3 - Image Layering:**
- `layer_original.jpg`, `layer_background.jpg`, `layer_secondary.jpg`, `layer_primary.jpg` - Layer progression
- `exploded_view.png` - Layer decomposition visualization

**Results Section:**
- `result1.jpg` through `result6.jpg` - Example results (add more as needed)

## Customization

### Updating Links

In `index.html`, update the placeholder links:

1. **Paper link** (line ~420):
   ```html
   <a href="YOUR_PAPER_URL" class="btn btn-primary">Download Paper</a>
   ```

2. **Code link** (line ~427):
   ```html
   <a href="YOUR_CODE_REPO_URL" class="btn btn-primary">View on GitHub</a>
   ```

3. **Supplementary link** (line ~434):
   ```html
   <a href="YOUR_SUPPLEMENTARY_URL" class="btn btn-primary">Download</a>
   ```

### Updating Author Information

In `_config.yml`:
- Update `author` field
- Update `author_email` field
- Update `url` with your actual domain

### Customizing Colors

In `styles.css`, modify the CSS variables at the top:
```css
:root {
    --primary-color: #1a73e8;       /* Main color */
    --secondary-color: #34a853;     /* Accent color */
    --accent-color: #fbbc04;        /* Highlight color */
    --text-dark: #202124;           /* Dark text */
    --text-light: #5f6368;          /* Light text */
}
```

## Features

- **Responsive Design** - Optimized for desktop, tablet, and mobile devices
- **Smooth Navigation** - Sticky navigation bar with smooth scrolling
- **Professional Layout** - Academic paper website design
- **Image Gallery** - Multiple sections for showcasing results
- **SEO Optimized** - Meta tags and structured content
- **Fast Loading** - No heavy frameworks or dependencies

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

This website template is provided as-is for presenting your research.

## Questions?

For setup issues or customization help, refer to:
- [GitHub Pages Documentation](https://pages.github.com/)
- [Jekyll Documentation](https://jekyllrb.com/)
