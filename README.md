# Luxe-Salon
# Luxe Salon (Flutter)

A graphic-rich salon app: animated splash, glass nav bar, magazine-style dashboard, and a booking flow.
All graphics are drawn in code (no image assets needed), so it runs as soon as you install it.

## Run it
1. Install Flutter: https://docs.flutter.dev/get-started/install
2. In this folder, create the platform folders once:
   `flutter create .`
   (this keeps your `lib/` and `pubspec.yaml`)
3. `flutter pub get`
4. `flutter run` (Android emulator, phone, or iOS simulator)

## Structure
- `lib/main.dart` : app entry and splash
- `lib/core/theme.dart` : palette, Playfair Display + Poppins, light/dark themes
- `lib/data/dummy_data.dart` : sample services, stylists, offers, reviews
- `lib/widgets/salon_graphics.dart` : blobs, sparkles, mirror and vine illustrations, before/after slider
- `lib/screens/home_screen.dart` : dashboard
- `lib/screens/booking_screen.dart` : booking flow

## Next steps
- Swap gradient tiles for real photos (add to `assets/` and declare in pubspec).
- Add Firebase (auth, Firestore, messaging) via `flutterfire configure`.
- Build the Services, Offers and Profile tabs, then the owner admin panel.
