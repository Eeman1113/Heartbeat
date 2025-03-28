
# Memories Of Us - Technical Documentation

## Project Overview

"Memories Of Us" is a responsive web application designed to display a personal photo gallery with a romantic aesthetic. The application features a custom loading screen with an animated heart, followed by a Pinterest-style masonry layout for displaying images. The gallery implements infinite scroll functionality that reuses previously loaded images when the user reaches the bottom of the page.

## Architecture Diagram
![architecture-diagram](https://github.com/user-attachments/assets/33cbdb32-1583-4917-8ce6-8a314bdf5679)
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <!-- Background -->
  <rect width="800" height="600" fill="#f8f3f0" />
  
  <!-- Dotted pattern background similar to the website -->
  <pattern id="dots" width="40" height="40" patternUnits="userSpaceOnUse">
    <circle cx="20" cy="20" r="1" fill="#e5d1cb" />
    <circle cx="0" cy="0" r="1" fill="#e5d1cb" />
    <circle cx="40" cy="40" r="1" fill="#e5d1cb" />
    <circle cx="0" cy="40" r="1" fill="#e5d1cb" />
    <circle cx="40" cy="0" r="1" fill="#e5d1cb" />
  </pattern>
  <rect width="800" height="600" fill="url(#dots)" />
  
  <!-- Title -->
  <text x="400" y="40" font-family="'Crimson Text', serif" font-size="24" text-anchor="middle" fill="#4a0f1d" font-weight="600">Memories Of Us - Architecture</text>
  
  <!-- Loading Screen Box -->
  <rect x="150" y="80" width="500" height="100" rx="10" ry="10" fill="#fff" stroke="#4a0f1d" stroke-width="2" />
  <text x="400" y="115" font-family="'Crimson Text', serif" font-size="18" text-anchor="middle" fill="#4a0f1d">Loading Screen</text>
  <text x="400" y="145" font-family="'Crimson Text', serif" font-size="14" text-anchor="middle" fill="#4a0f1d" font-style="italic">(Animated heart with text - 3 second minimum display)</text>
  
  <!-- Arrow down -->
  <line x1="400" y1="180" x2="400" y2="210" stroke="#4a0f1d" stroke-width="2" />
  <polygon points="400,220 395,210 405,210" fill="#4a0f1d" />
  
  <!-- Main Content Box -->
  <rect x="100" y="220" width="600" height="300" rx="10" ry="10" fill="#fff" stroke="#4a0f1d" stroke-width="2" />
  <text x="400" y="250" font-family="'Crimson Text', serif" font-size="18" text-anchor="middle" fill="#4a0f1d">Main Content</text>
  
  <!-- Gallery Box -->
  <rect x="150" y="270" width="500" height="80" rx="8" ry="8" fill="#f8f3f0" stroke="#4a0f1d" stroke-width="1.5" stroke-dasharray="5,3" />
  <text x="400" y="300" font-family="'Crimson Text', serif" font-size="16" text-anchor="middle" fill="#4a0f1d">Gallery</text>
  <text x="400" y="325" font-family="'Crimson Text', serif" font-size="14" text-anchor="middle" fill="#4a0f1d" font-style="italic">(Masonry layout with dynamically loaded images)</text>
  
  <!-- Arrow down -->
  <line x1="400" y1="350" x2="400" y2="370" stroke="#4a0f1d" stroke-width="2" />
  <polygon points="400,380 395,370 405,370" fill="#4a0f1d" />
  
  <!-- Infinite Scroll Box -->
  <rect x="150" y="380" width="500" height="60" rx="8" ry="8" fill="#f8f3f0" stroke="#4a0f1d" stroke-width="1.5" />
  <text x="400" y="410" font-family="'Crimson Text', serif" font-size="16" text-anchor="middle" fill="#4a0f1d">Infinite Scroll System</text>
  <text x="400" y="430" font-family="'Crimson Text', serif" font-size="12" text-anchor="middle" fill="#4a0f1d" font-style="italic">(Detects scroll position and adds more images as needed)</text>
  
  <!-- Image Store Circle -->
  <circle cx="650" cy="500" r="70" fill="#fff" stroke="#4a0f1d" stroke-width="2" />
  <text x="650" y="490" font-family="'Crimson Text', serif" font-size="16" text-anchor="middle" fill="#4a0f1d">Loaded</text>
  <text x="650" y="510" font-family="'Crimson Text', serif" font-size="16" text-anchor="middle" fill="#4a0f1d">Images</text>
  <text x="650" y="530" font-family="'Crimson Text', serif" font-size="12" text-anchor="middle" fill="#4a0f1d" font-style="italic">(Cache)</text>
  
  <!-- Arrow from Infinite Scroll to Image Store -->
  <line x1="480" y1="440" x2="600" y2="480" stroke="#4a0f1d" stroke-width="2" stroke-dasharray="5,3" />
  <polygon points="610,485 595,485 600,475" fill="#4a0f1d" />
  
  <!-- Arrow from Image Store to Infinite Scroll -->
  <line x1="600" y1="460" x2="480" y2="420" stroke="#4a0f1d" stroke-width="2" />
  <polygon points="470,415 485,415 480,425" fill="#4a0f1d" />
  
  <!-- Image Directory Box -->
  <rect x="150" y="470" width="200" height="80" rx="8" ry="8" fill="#fff" stroke="#4a0f1d" stroke-width="2" />
  <text x="250" y="500" font-family="'Crimson Text', serif" font-size="16" text-anchor="middle" fill="#4a0f1d">./image/</text>
  <text x="250" y="525" font-family="'Crimson Text', serif" font-size="14" text-anchor="middle" fill="#4a0f1d" font-style="italic">(Source Files)</text>
  
  <!-- Arrow from Image Directory to Image Store -->
  <line x1="350" y1="500" x2="570" y2="500" stroke="#4a0f1d" stroke-width="2" />
  <polygon points="580,500 570,495 570,505" fill="#4a0f1d" />
  
  <!-- Legend Box -->
  <rect x="50" y="555" width="700" height="35" rx="5" ry="5" fill="rgba(255,255,255,0.7)" stroke="#4a0f1d" stroke-width="1" />
  
  <!-- Legend Items -->
  <line x1="70" y1="572" x2="90" y2="572" stroke="#4a0f1d" stroke-width="2" />
  <text x="100" y="575" font-family="'Crimson Text', serif" font-size="12" fill="#4a0f1d">Data Flow</text>
  
  <line x1="180" y1="572" x2="200" y2="572" stroke="#4a0f1d" stroke-width="2" stroke-dasharray="5,3" />
  <text x="210" y="575" font-family="'Crimson Text', serif" font-size="12" fill="#4a0f1d">Reference Flow</text>
  
  <rect x="320" y="565" width="15" height="15" rx="3" ry="3" fill="#fff" stroke="#4a0f1d" stroke-width="1.5" />
  <text x="345" y="575" font-family="'Crimson Text', serif" font-size="12" fill="#4a0f1d">Component</text>
  
  <rect x="430" y="565" width="15" height="15" rx="3" ry="3" fill="#f8f3f0" stroke="#4a0f1d" stroke-width="1.5" stroke-dasharray="5,3" />
  <text x="455" y="575" font-family="'Crimson Text', serif" font-size="12" fill="#4a0f1d">Dynamic Content</text>
  
  <circle cx="530" cy="572" r="7" fill="#fff" stroke="#4a0f1d" stroke-width="1.5" />
  <text x="550" y="575" font-family="'Crimson Text', serif" font-size="12" fill="#4a0f1d">Data Store</text>
  
  <!-- Heart icon -->
  <g transform="translate(630, 565)">
    <rect width="15" height="15" fill="transparent" />
    <path d="M7.5,14 C7.5,14 0,8 0,4 C0,1.5 1.5,0 3.5,0 C5,0 7.5,2 7.5,2 C7.5,2 10,0 11.5,0 C13.5,0 15,1.5 15,4 C15,8 7.5,14 7.5,14 Z" fill="#4a0f1d" />
  </g>
  <text x="655" y="575" font-family="'Crimson Text', serif" font-size="12" fill="#4a0f1d">Animation</text>
</svg>e-diagram.svg…]()

```
┌─────────────────────────────────┐
│           Application           │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│         Loading Screen          │──┐
│  (Displays for minimum 3 secs)  │  │
└───────────────┬─────────────────┘  │
                │                    │ Transition
                ▼                    │ Animation
┌─────────────────────────────────┐  │
│          Main Content           │◄─┘
│ ┌─────────────────────────────┐ │
│ │           Gallery           │ │
│ │   (Masonry layout with      │ │
│ │     lazy-loaded images)     │ │
│ └─────────────┬───────────────┘ │
│               │                 │
│               ▼                 │
│ ┌─────────────────────────────┐ │
│ │       Infinite Scroll       │ │
│ │  (Detects when user nears   │ │
│ │   bottom of page & loads    │ │
│ │       additional items)     │ │
│ └─────────────┬───────────────┘ │
│               │                 │
│               ▼                 │
│ ┌─────────────────────────────┐ │
│ │  Loading More Indicator     │ │
│ │  (Skeleton UI displayed     │ │
│ │   during content loading)   │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

## Component Structure Diagram

```
┌─ Body ───────────────────────────────┐
│                                       │
│  ┌─ Loading Screen ─────────────────┐ │
│  │                                  │ │
│  │  ┌─ Card ───────────────────┐    │ │
│  │  │                          │    │ │
│  │  │    ┌─ Blur Shape ─┐      │    │ │
│  │  │    │ (Heart Anim) │      │    │ │
│  │  │    └──────────────┘      │    │ │
│  │  │                          │    │ │
│  │  │    ┌─ Text ────────┐     │    │ │
│  │  │    │ (Quote)       │     │    │ │
│  │  │    └───────────────┘     │    │ │
│  │  │                          │    │ │
│  │  └──────────────────────────┘    │ │
│  │                                  │ │
│  └──────────────────────────────────┘ │
│                                       │
│  ┌─ Main Content ───────────────────┐ │
│  │                                  │ │
│  │  ┌─ Title ───────────────────┐   │ │
│  │  └───────────────────────────┘   │ │
│  │                                  │ │
│  │  ┌─ Gallery ─────────────────┐   │ │
│  │  │                           │   │ │
│  │  │  ┌─ Gallery Item ─────┐   │   │ │
│  │  │  │ ┌─ Image ─────┐    │   │   │ │
│  │  │  │ └─────────────┘    │   │   │ │
│  │  │  └───────────────────┘   │   │ │
│  │  │                           │   │ │
│  │  │  ┌─ Gallery Item ─────┐   │   │ │
│  │  │  │ ┌─ Image ─────┐    │   │   │ │
│  │  │  │ └─────────────┘    │   │   │ │
│  │  │  └───────────────────┘   │   │ │
│  │  │                           │   │ │
│  │  │  ...                      │   │ │
│  │  │                           │   │ │
│  │  └───────────────────────────┘   │ │
│  │                                  │ │
│  │  ┌─ Loading More ──────────────┐ │ │
│  │  │ ┌─ Skeleton Container ────┐ │ │ │
│  │  │ │ ┌─ Skeleton Item ────┐  │ │ │ │
│  │  │ │ └────────────────────┘  │ │ │ │
│  │  │ │ ┌─ Skeleton Item ────┐  │ │ │ │
│  │  │ │ └────────────────────┘  │ │ │ │
│  │  │ │ ┌─ Skeleton Item ────┐  │ │ │ │
│  │  │ │ └────────────────────┘  │ │ │ │
│  │  │ └──────────────────────┘  │ │ │ │
│  │  └────────────────────────────┘ │ │
│  │                                  │ │
│  └──────────────────────────────────┘ │
│                                       │
└───────────────────────────────────────┘
```

## Data Flow Diagram

```
┌───────────────────┐     ┌─────────────────────┐
│                   │     │                     │
│  Page Load Event  │────►│  Display Loading    │
│                   │     │       Screen        │
└───────────────────┘     └─────────┬───────────┘
                                    │
                                    │ After 3 seconds
                                    ▼
┌───────────────────┐     ┌─────────────────────┐
│                   │     │                     │
│ loadedImagePaths  │◄────┤  Load Images from   │
│     Array         │     │   ./image Directory │
│                   │     │                     │
└─────────┬─────────┘     └─────────┬───────────┘
          │                         │
          │                         │ Images loaded
          │                         ▼
          │               ┌─────────────────────┐
          │               │                     │
          │               │  Display Images     │
          │               │  in Gallery         │
          │               │                     │
          │               └─────────┬───────────┘
          │                         │
          │                         │ User scrolls
          │                         ▼
          │               ┌─────────────────────┐
          │               │  Detect Near Bottom │
          │               │  of Page            │
          │               └─────────┬───────────┘
          │                         │
          │                         │ If near bottom
          │                         ▼
          │               ┌─────────────────────┐
          └───────────────►  Shuffle and Select │
                          │  Random Images      │
                          │  from Loaded Images │
                          └─────────┬───────────┘
                                    │
                                    ▼
                          ┌─────────────────────┐
                          │  Add More Images    │
                          │  to Gallery         │
                          └─────────────────────┘
```

## Technical Details

### HTML Structure

The application consists of two main sections:
1. **Loading Screen** - A minimal interface with an animated heart shape and a quote
2. **Main Content** - Contains the gallery of images with infinite scroll functionality

### CSS Features

- **Animations**: Multiple custom keyframe animations including:
  - `heartbeat` - For the pulsating heart on the loading screen
  - `fadeIn` - For smooth transition of elements
  - `floatIn` - For gallery items appearing
  - `pulse` - For subtle shadow effects
  - `shimmer` - For the loading skeleton items

- **Responsive Design**:
  - Adapts to different screen sizes using media queries
  - Uses CSS Grid and Flexbox for layouts
  - Employs CSS columns for the masonry layout
  - Utilizes `clamp()` for responsive typography

- **Design System**:
  - Custom color palette with bordeaux (#4a0f1d) as the primary color
  - Subtle textured background using radial gradients
  - Custom-styled loading skeletons inspired by shadcn/ui
  - Consistent box-shadow styling

### JavaScript Functionality

#### Loading Screen Handling
- Displays for a minimum of 3 seconds
- Uses `setTimeout` for controlling transitions
- Smooth opacity transitions between screens

#### Image Loading System
- Dynamic image detection from the `/image` directory
- Tests multiple file naming patterns and extensions
- Tracks successful image loads with the `loadedImagePaths` array
- Implements lazy loading with the `loading="lazy"` attribute

#### Infinite Scroll Implementation
- Event listener for scroll position
- Detects when user approaches bottom of page (500px threshold)
- Shows skeleton loading UI during content fetch
- Shuffles previously loaded images for variety
- Randomly selects 5-10 images to add per load

#### Error Handling
- Graceful fallback when images aren't found
- Custom message when no images are detected
- Console logging for troubleshooting

## Browser Compatibility

The application uses modern CSS features including:
- CSS Grid
- Flexbox
- CSS Variables
- CSS Animations
- `clamp()` for responsive sizing

These features are supported in all modern browsers, but may require fallbacks for IE11 or older browsers.

## Performance Considerations

- **Lazy Loading**: Images use the native `loading="lazy"` attribute
- **Animation Performance**: Uses transform and opacity for smooth animations
- **Throttled Scroll Events**: Uses natural scroll debouncing
- **Image Reuse**: Recycles already-loaded images during infinite scroll
- **Minimal DOM Updates**: Batches image additions for better performance

## Setup Instructions

1. Clone the repository
2. Place your images in the `./image` directory
   - The script will attempt to find images with common naming patterns:
     - `1.jpg`, `2.jpg`, `3.jpg`, etc.
     - `image1.jpg`, `image2.jpg`, etc.
     - `photo1.jpg`, `photo2.jpg`, etc.
     - `img1.jpg`, `img2.jpg`, etc.
     - `pic1.jpg`, `pic2.jpg`, etc.
   - Supported extensions: jpg, jpeg, png, gif, webp, bmp, svg
3. Open `index.html` in a browser

## Customization Options

- Update the heart color by changing the `#4a0f1d` color values
- Modify the background pattern by adjusting the radial gradient properties
- Change the fonts by updating the Google Fonts import and font-family properties
- Adjust animation timings by modifying the keyframe percentages and animation durations
- Update the loading screen quote in the HTML
