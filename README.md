# Memories Of Us - Technical Documentation

## Project Overview

"Memories Of Us" is a responsive web application designed to display a personal photo gallery with a romantic aesthetic. The application features a custom loading screen with an animated heart, followed by a Pinterest-style masonry layout for displaying images. The gallery implements infinite scroll functionality that reuses previously loaded images when the user reaches the bottom of the page.

## Architecture Diagram

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