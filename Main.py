import 'package:flutter/material.dart';
import 'core/theme.dart';
import 'screens/home_screen.dart';
import 'widgets/salon_graphics.dart';

void main() => runApp(const LuxeSalonApp());

class LuxeSalonApp extends StatelessWidget {
  const LuxeSalonApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Luxe Salon',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light(),
      darkTheme: AppTheme.dark(),
      themeMode: ThemeMode.system,
      home: const SplashScreen(),
    );
  }
}

/// Splash: animated sparkles around the logo, then fades into the dashboard.
class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});
  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Future.delayed(const Duration(milliseconds: 2400), () {
      if (!mounted) return;
      Navigator.of(context).pushReplacement(PageRouteBuilder(
        transitionDuration: const Duration(milliseconds: 700),
        pageBuilder: (_, __, ___) => const HomeScreen(),
        transitionsBuilder: (_, anim, __, child) =>
            FadeTransition(opacity: anim, child: child),
      ));
    });
  }

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    return Scaffold(
      body: Stack(children: [
        const BlobBackground(),
        Center(
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            SizedBox(
              width: 220,
              height: 220,
              child: Stack(alignment: Alignment.center, children: [
                const Positioned.fill(child: AnimatedSparkles()),
                SizedBox(
                    width: 130,
                    height: 150,
                    child: CustomPaint(
                        painter: MirrorPainter(color: AppColors.roseGold))),
              ]),
            ),
            Text('Luxe Salon', style: t.headlineMedium),
            const SizedBox(height: 6),
            Text('Beauty, beautifully booked', style: t.bodyMedium),
          ]),
        ),
      ]),
    );
  }
}
