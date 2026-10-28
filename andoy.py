
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#080d19">
    <title>Jhulian Claire B. Andoy | Portfolio</title>

    <style>
        :root {
            --bg: #080d19;
            --panel: rgba(17, 26, 43, 0.86);
            --mint: #9bf5d0;
            --blue: #8bbcff;
            --purple: #c3a5ff;
            --white: #f4f7ff;
            --muted: #a8b4c9;
            --border: rgba(255, 255, 255, .12);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: var(--bg);
            color: var(--white);
            line-height: 1.7;
            overflow-x: hidden;
        }

        button, a {
            -webkit-tap-highlight-color: transparent;
        }

        button {
            font: inherit;
        }

        a {
            color: inherit;
        }

        /* Background graphics */

        .background-art {
            position: fixed;
            inset: 0;
            overflow: hidden;
            pointer-events: none;
            z-index: -1;
            background:
                radial-gradient(
                    ellipse at 10% 10%,
                    rgba(25, 95, 88, .20),
                    transparent 42%
                ),
                radial-gradient(
                    ellipse at 90% 30%,
                    rgba(91, 65, 150, .18),
                    transparent 42%
                ),
                var(--bg);
        }

        .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(2px);
            opacity: .22;
            animation: float 12s ease-in-out infinite alternate;
        }

        .orb-one {
            width: 260px;
            height: 260px;
            background: var(--mint);
            top: 10%;
            left: -130px;
        }

        .orb-two {
            width: 340px;
            height: 340px;
            background: var(--purple);
            right: -180px;
            top: 40%;
            animation-delay: -4s;
        }

        .orb-three {
            width: 180px;
            height: 180px;
            background: var(--blue);
            left: 35%;
            bottom: -100px;
            animation-delay: -7s;
        }

        .decor-grid {
            position: absolute;
            inset: 0;
            opacity: .07;
            background-image:
                linear-gradient(rgba(255,255,255,.15) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,.15) 1px, transparent 1px);
            background-size: 45px 45px;
            mask-image: linear-gradient(to bottom, black, transparent 90%);
        }

        .progress-track {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            z-index: 300;
            background: transparent;
        }

        .progress-bar {
            height: 100%;
            width: 0;
            background: linear-gradient(
                90deg, var(--mint), var(--blue), var(--purple)
            );
            box-shadow: 0 0 12px rgba(155,245,208,.6);
        }

        /* Welcome screen */

        .welcome {
            min-height: 100vh;
            min-height: 100svh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 25px;
            text-align: center;
            position: relative;
            isolation: isolate;
            background:
                radial-gradient(circle at 15% 15%, #153b42, transparent 42%),
                radial-gradient(circle at 90% 85%, #2c204d, transparent 42%),
                var(--bg);
        }

        .welcome::before,
        .welcome::after {
            content: "";
            position: absolute;
            width: 180px;
            height: 180px;
            border: 1px solid rgba(155,245,208,.20);
            border-radius: 35px;
            transform: rotate(35deg);
            pointer-events: none;
            z-index: -1;
        }

        .welcome::before {
            top: 8%;
            left: 5%;
        }

        .welcome::after {
            bottom: 8%;
            right: 5%;
            border-color: rgba(195,165,255,.24);
            transform: rotate(55deg);
        }

        .welcome-card {
            width: 100%;
            max-width: 700px;
            padding: 42px 28px;
            position: relative;
            overflow: hidden;
            border: 1px solid var(--border);
            border-radius: 30px;
            background: rgba(13, 22, 38, .78);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            box-shadow:
                0 25px 80px rgba(0,0,0,.4),
                0 0 45px rgba(155,245,208,.06);
            animation: rise-in .9s ease both;
        }

        .welcome-card::before {
            content: "";
            position: absolute;
            width: 250px;
            height: 250px;
            right: -140px;
            top: -140px;
            border-radius: 50%;
            background: var(--purple);
            filter: blur(90px);
            opacity: .18;
            pointer-events: none;
        }

        .welcome-photo-wrap {
            position: relative;
            width: 190px;
            height: 190px;
            margin: 0 auto 25px;
        }

        .welcome-photo-ring {
            position: absolute;
            inset: -9px;
            border-radius: 50%;
            border: 2px dashed rgba(155,245,208,.65);
            animation: rotate-ring 20s linear infinite;
        }

        .welcome-photo {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            border-radius: 50%;
            border: 4px solid var(--mint);
            box-shadow: 0 0 35px rgba(155,245,208,.24);
        }

        .eyebrow {
            color: var(--mint);
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .welcome h1 {
            font-size: clamp(29px, 6vw, 48px);
            line-height: 1.2;
            margin-bottom: 15px;
        }

        .welcome-description {
            color: var(--muted);
            margin-bottom: 28px;
        }

        .gradient-text {
            background: linear-gradient(
                90deg, var(--mint), var(--blue), var(--purple)
            );
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .primary-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            border: none;
            border-radius: 30px;
            padding: 14px 25px;
            background: linear-gradient(100deg, var(--mint), #b8f8e3);
            color: #07130f;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 0 25px rgba(155,245,208,.12);
            transition: transform .25s, box-shadow .25s;
        }

        .primary-button:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(155,245,208,.25);
        }

        .primary-button:focus-visible,
        .back-button:focus-visible,
        a:focus-visible {
            outline: 2px solid var(--mint);
            outline-offset: 4px;
        }

        .welcome-note {
            color: var(--muted);
            font-size: 12px;
            margin-top: 23px;
            letter-spacing: 1px;
        }

        /* Dashboard */

        .dashboard {
            display: none;
            animation: rise-in .55s ease both;
        }

        .topbar {
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
            padding: 15px 7%;
            background: rgba(8,13,25,.88);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--border);
        }

        .brand {
            font-size: 19px;
            font-weight: 800;
            color: var(--mint);
            letter-spacing: 1px;
        }

        .brand span {
            color: var(--white);
        }

        .back-button {
            border: 1px solid rgba(155,245,208,.4);
            background: rgba(155,245,208,.06);
            color: var(--mint);
            padding: 8px 15px;
            border-radius: 25px;
            cursor: pointer;
            transition: .25s;
        }

        .back-button:hover {
            background: var(--mint);
            color: #07130f;
        }

        /* Hero */

        .hero {
            min-height: 78vh;
            min-height: 78svh;
            display: flex;
            align-items: center;
            padding: 85px 9%;
            position: relative;
            overflow: hidden;
            background:
                radial-gradient(circle at 82% 35%, rgba(48,83,125,.25), transparent 34%),
                radial-gradient(circle at 8% 90%, rgba(20,92,76,.18), transparent 35%);
        }

        .hero-content {
            max-width: 850px;
            position: relative;
            z-index: 2;
        }

        .status-label {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            padding: 7px 13px;
            margin-bottom: 24px;
            border: 1px solid rgba(155,245,208,.25);
            border-radius: 25px;
            color: var(--mint);
            background: rgba(155,245,208,.06);
            font-size: 12px;
            letter-spacing: 1px;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--mint);
            box-shadow: 0 0 12px var(--mint);
        }

        .hero h2 {
            font-size: clamp(40px, 7.5vw, 76px);
            line-height: 1.12;
            margin-bottom: 23px;
            letter-spacing: -2px;
        }

        .hero p {
            max-width: 650px;
            color: var(--muted);
            font-size: clamp(15px, 2vw, 18px);
            margin-bottom: 30px;
        }

        .hero-decoration {
            position: absolute;
            right: 9%;
            top: 50%;
            width: 220px;
            height: 220px;
            border: 1px solid rgba(155,245,208,.18);
            border-radius: 45px;
            transform: translateY(-50%) rotate(35deg);
            box-shadow:
                0 0 0 25px rgba(155,245,208,.025),
                0 0 0 50px rgba(139,188,255,.02);
            animation: float 7s ease-in-out infinite alternate;
        }

        .hero-decoration::before,
        .hero-decoration::after {
            content: "";
            position: absolute;
            border-radius: 50%;
            border: 1px solid rgba(195,165,255,.5);
        }

        .hero-decoration::before {
            inset: 30px;
        }

        .hero-decoration::after {
            inset: 65px;
            background: rgba(155,245,208,.04);
        }

        .hero-bottom {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 35px;
        }

        .mini-stat {
            padding: 12px 17px;
            border-left: 2px solid var(--mint);
            background: rgba(255,255,255,.035);
            border-radius: 0 10px 10px 0;
        }

        .mini-stat strong {
            display: block;
            font-size: 16px;
            color: var(--white);
        }

        .mini-stat span {
            color: var(--muted);
            font-size: 12px;
        }

        /* Sections */

        .section {
            padding: 80px 9%;
            scroll-margin-top: 75px;
            position: relative;
        }

        .section:nth-of-type(even) {
            background: rgba(255,255,255,.018);
        }

        .section-heading {
            margin-bottom: 35px;
        }

        .section-number {
            display: inline-block;
            color: var(--mint);
            font-size: 12px;
            letter-spacing: 3px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .section-title {
            font-size: clamp(29px, 4.5vw, 40px);
            line-height: 1.2;
            margin-bottom: 12px;
        }

        .section-description {
            color: var(--muted);
            max-width: 650px;
        }

        .heading-line {
            width: 75px;
            height: 4px;
            border-radius: 5px;
            margin-top: 18px;
            background: linear-gradient(90deg, var(--mint), var(--purple));
        }

        /* Glass cards */

        .card {
            min-width: 0;
            padding: 27px;
            border: 1px solid var(--border);
            border-radius: 22px;
            background: linear-gradient(
                145deg,
                rgba(22,34,54,.91),
                rgba(12,19,33,.92)
            );
            box-shadow: 0 12px 35px rgba(0,0,0,.12);
            transition: transform .3s, border-color .3s, box-shadow .3s;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: rgba(155,245,208,.4);
            box-shadow: 0 18px 40px rgba(0,0,0,.22);
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 22px;
        }

        .card h3 {
            color: var(--mint);
            font-size: 19px;
            margin-bottom: 10px;
        }

        .card p,
        .card li {
            color: var(--muted);
            overflow-wrap: anywhere;
        }

        .card p + p {
            margin-top: 5px;
        }

        .card strong {
            color: var(--white);
        }

        .card-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 53px;
            height: 53px;
            margin-bottom: 19px;
            border: 1px solid rgba(155,245,208,.22);
            border-radius: 16px;
            background: linear-gradient(
                135deg,
                rgba(155,245,208,.14),
                rgba(139,188,255,.08)
            );
            font-size: 25px;
        }

        /* Personal information */

        .personal-layout {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(0, 1.5fr);
            gap: 25px;
            align-items: stretch;
        }

        .profile-side {
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 300px;
            background:
                radial-gradient(circle at 100% 0%, rgba(155,245,208,.12), transparent 45%),
                var(--panel);
        }

        .profile-symbol {
            width: 85px;
            height: 85px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 26px;
            margin-bottom: 22px;
            font-size: 37px;
            color: var(--mint);
            background: linear-gradient(
                135deg,
                rgba(155,245,208,.16),
                rgba(195,165,255,.14)
            );
            border: 1px solid rgba(155,245,208,.3);
        }

        .profile-side h3 {
            color: var(--white);
            font-size: 24px;
            margin-bottom: 8px;
        }

        .profile-side p {
            color: var(--muted);
        }

        .info-list {
            display: grid;
            gap: 12px;
            align-content: center;
        }

        .info-item {
            padding: 14px 17px;
            border: 1px solid rgba(255,255,255,.06);
            border-radius: 13px;
            background: rgba(255,255,255,.035);
            overflow-wrap: anywhere;
        }

        .info-item strong {
            color: var(--mint);
            display: block;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 3px;
        }

        /* Education timeline */

        .education-timeline {
            position: relative;
            display: grid;
            gap: 22px;
            padding-left: 25px;
        }

        .education-timeline::before {
            content: "";
            position: absolute;
            top: 15px;
            bottom: 15px;
            left: 6px;
            width: 2px;
            background: linear-gradient(
                to bottom, var(--mint), var(--blue), var(--purple)
            );
            opacity: .65;
        }

        .education-card {
            position: relative;
        }

        .education-card::before {
            content: "";
            position: absolute;
            width: 13px;
            height: 13px;
            left: -26px;
            top: 30px;
            border-radius: 50%;
            background: var(--mint);
            border: 3px solid var(--bg);
            box-shadow: 0 0 15px rgba(155,245,208,.5);
        }

        .education-year {
            display: inline-block;
            padding: 4px 11px;
            margin-bottom: 12px;
            border-radius: 20px;
            color: var(--mint);
            background: rgba(155,245,208,.08);
            border: 1px solid rgba(155,245,208,.2);
            font-size: 12px;
            font-weight: bold;
        }

        /* Skills */

        .skill-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .skill-card {
            padding: 23px 18px;
            border-radius: 19px;
            border: 1px solid var(--border);
            background: rgba(17,26,43,.76);
            text-align: center;
            transition: transform .25s, border-color .25s;
        }

        .skill-card:hover {
            transform: translateY(-5px);
            border-color: rgba(155,245,208,.5);
        }

        .skill-icon {
            width: 57px;
            height: 57px;
            margin: 0 auto 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 18px;
            font-size: 26px;
            background: linear-gradient(
                135deg,
                rgba(155,245,208,.14),
                rgba(195,165,255,.12)
            );
        }

        .skill-card h3 {
            font-size: 15px;
            line-height: 1.5;
            color: var(--white);
        }

        .skill-card p {
            color: var(--muted);
            font-size: 12px;
            margin-top: 5px;
        }

        /* Certificates: photos only, no captions */

        .certificate-gallery {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 24px;
            align-items: start;
        }

        .certificate-frame {
            position: relative;
            overflow: hidden;
            padding: 8px;
            border: 1px solid rgba(155,245,208,.18);
            border-radius: 17px;
            background: rgba(255,255,255,.035);
            box-shadow: 0 15px 35px rgba(0,0,0,.2);
            transition: transform .3s, border-color .3s;
        }

        .certificate-frame:hover {
            transform: translateY(-5px);
            border-color: rgba(155,245,208,.5);
        }

        .certificate-gallery img {
            display: block;
            width: 100%;
            height: auto;
            object-fit: contain;
            border-radius: 10px;
            background: var(--panel);
        }

        /* Social media */

        .social-links {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            min-width: 0;
            padding: 19px 15px;
            border-radius: 17px;
            text-decoration: none;
            color: var(--white);
            background: linear-gradient(
                145deg, rgba(22,34,54,.92), rgba(12,19,33,.92)
            );
            border: 1px solid var(--border);
            transition: transform .25s, border-color .25s, color .25s;
        }

        .social-links a:hover {
            transform: translateY(-5px);
            color: var(--mint);
            border-color: var(--mint);
        }

        .social-icon {
            font-size: 23px;
        }

        .social-name {
            font-weight: bold;
            overflow-wrap: anywhere;
        }

        .closing-card {
            margin-top: 45px;
            padding: 35px 25px;
            text-align: center;
            border: 1px solid rgba(155,245,208,.2);
            border-radius: 23px;
            background:
                radial-gradient(circle at 0% 100%, rgba(155,245,208,.08), transparent 45%),
                radial-gradient(circle at 100% 0%, rgba(195,165,255,.10), transparent 45%),
                rgba(17,26,43,.65);
        }

        .closing-card h3 {
            font-size: clamp(22px, 4vw, 30px);
            margin-bottom: 8px;
        }

        .closing-card p {
            color: var(--muted);
        }

        footer {
            padding: 30px 18px;
            text-align: center;
            color: var(--muted);
            border-top: 1px solid var(--border);
            background: rgba(5,9,17,.5);
            font-size: 13px;
        }

        footer .footer-name {
            color: var(--mint);
            font-weight: bold;
        }

        .back-to-top {
            position: fixed;
            right: 20px;
            bottom: 20px;
            width: 44px;
            height: 44px;
            display: none;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(155,245,208,.4);
            border-radius: 50%;
            background: rgba(17,26,43,.95);
            color: var(--mint);
            font-size: 21px;
            cursor: pointer;
            z-index: 90;
            box-shadow: 0 5px 20px rgba(0,0,0,.25);
        }

        .back-to-top:hover {
            background: var(--mint);
            color: var(--bg);
        }

        /* Animations */

        @keyframes rise-in {
            from {
                opacity: 0;
                transform: translateY(18px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes float {
            from {
                transform: translateY(0) rotate(0deg);
            }
            to {
                transform: translateY(-24px) rotate(12deg);
            }
        }

        @keyframes rotate-ring {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }

        /* Responsive layout */

        @media (max-width: 850px) {
            .hero-decoration {
                right: -100px;
                opacity: .4;
            }

            .personal-layout {
                grid-template-columns: 1fr;
            }

            .profile-side {
                min-height: 230px;
            }

            .skill-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 600px) {
            .welcome-card {
                padding: 35px 20px;
                border-radius: 24px;
            }

            .welcome-photo-wrap {
                width: 150px;
                height: 150px;
            }

            .welcome::before,
            .welcome::after {
                width: 100px;
                height: 100px;
            }

            .topbar {
                padding: 13px 5%;
            }

            .brand {
                font-size: 16px;
            }

            .back-button {
                font-size: 12px;
                padding: 8px 11px;
            }

            .hero {
                min-height: 70vh;
                min-height: 70svh;
                padding: 65px 7%;
            }

            .hero h2 {
                letter-spacing: -1px;
            }

            .hero-decoration {
                width: 150px;
                height: 150px;
                right: -95px;
                opacity: .25;
            }

            .hero-bottom {
                gap: 9px;
            }

            .mini-stat {
                padding: 10px 12px;
            }

            .section {
                padding: 58px 7%;
            }

            .card-grid,
            .certificate-gallery {
                grid-template-columns: 1fr;
            }

            .skill-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 12px;
            }

            .skill-card {
                padding: 20px 12px;
            }

            .social-links {
                grid-template-columns: 1fr;
                gap: 12px;
            }

            .social-links a {
                justify-content: flex-start;
                padding: 16px 20px;
            }

            .card {
                padding: 22px;
            }

            .closing-card {
                padding: 28px 18px;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                scroll-behavior: auto !important;
                animation-duration: .01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: .01ms !important;
            }
        }
    </style>
</head>

<body>
    <div class="background-art" aria-hidden="true">
        <div class="decor-grid"></div>
        <div class="orb orb-one"></div>
        <div class="orb orb-two"></div>
        <div class="orb orb-three"></div>
    </div>

    <div class="progress-track" aria-hidden="true">
        <div class="progress-bar" id="progressBar"></div>
    </div>

    <!-- WELCOME SCREEN -->
    <section class="welcome" id="welcome">
        <div class="welcome-card">

            <div class="welcome-photo-wrap">
                <div class="welcome-photo-ring"></div>
                <img
                    class="welcome-photo"
                    src="{{ url_for('static', filename='images/andoy.jpg') }}"
                    alt="Jhulian Claire B. Andoy"
                >
            </div>

            <p class="eyebrow">✦ Welcome to my portfolio ✦</p>

            <h1>
                Jhulian Claire B.<br>
                <span class="gradient-text">Andoy</span>
            </h1>

            <p class="welcome-description">
                Bachelor of Science in Information Technology Student
            </p>

            <button class="primary-button" onclick="openPortfolio()">
                ENTER MY PORTFOLIO <span aria-hidden="true">→</span>
            </button>

            <p class="welcome-note">LEARN • CREATE • GROW</p>
        </div>
    </section>

    <!-- MAIN PORTFOLIO -->
    <div class="dashboard" id="dashboard">

        <header class="topbar">
            <div class="brand">JCA<span>.</span> Portfolio</div>

            <button class="back-button" onclick="returnToWelcome()">
                ← Welcome Screen
            </button>
        </header>

        <main>
            <!-- HOME -->
            <section class="hero" id="home">
                <div class="hero-content">

                    <div class="status-label">
                        <span class="status-dot"></span>
                        PERSONAL PORTFOLIO
                    </div>

                    <p class="eyebrow">Hello and welcome!</p>

                    <h2>
                        Hello, I'm<br>
                        <span class="gradient-text">
                            Jhulian Claire Andoy
                        </span>
                    </h2>

                    <p>
                        I am a Bachelor of Science in Information Technology
                        student who enjoys learning about technology,
                        solving problems, and exploring creative ideas.
                        This portfolio presents my educational background,
                        skills, and interests.
                    </p>

                    <button
                        class="primary-button"
                        onclick="scrollToSection('personal')"
                    >
                        Explore My Profile <span aria-hidden="true">↘</span>
                    </button>

                    <div class="hero-bottom">
                        <div class="mini-stat">
                            <strong>BSIT</strong>
                            <span>Course</span>
                        </div>

                        <div class="mini-stat">
                            <strong>BSIT-2B</strong>
                            <span>Section</span>
                        </div>

                        <div class="mini-stat">
                            <strong>2025–2029</strong>
                            <span>College Years</span>
                        </div>
                    </div>
                </div>

                <div class="hero-decoration" aria-hidden="true"></div>
            </section>

            <!-- PERSONAL INFORMATION -->
            <section class="section" id="personal">
                <div class="section-heading">
                    <span class="section-number">01 / ABOUT ME</span>
                    <h2 class="section-title">Personal Information</h2>
                    <p class="section-description">
                        A little information about me, my studies, and my interests.
                    </p>
                    <div class="heading-line"></div>
                </div>

                <div class="personal-layout">
                    <article class="card profile-side">
                        <div class="profile-symbol" aria-hidden="true">✦</div>
                        <h3>Jhulian Claire B. Andoy</h3>
                        <p>
                            Information Technology student with an interest
                            in learning, problem-solving, and technology.
                        </p>
                    </article>

                    <div class="card">
                        <div class="info-list">
                            <div class="info-item">
                                <strong>Full Name</strong>
                                Jhulian Claire B. Andoy
                            </div>

                            <div class="info-item">
                                <strong>Age</strong>
                                19 years old
                            </div>

                            <div class="info-item">
                                <strong>Course</strong>
                                Bachelor of Science in Information Technology
                            </div>

                            <div class="info-item">
                                <strong>School</strong>
                                Torres Capitol College, Inc.
                            </div>

                            <div class="info-item">
                                <strong>Section</strong>
                                BSIT-2B
                            </div>

                            <div class="info-item">
                                <strong>Interests</strong>
                                Reading and solving interesting problems
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- EDUCATION -->
            <section class="section" id="education">
                <div class="section-heading">
                    <span class="section-number">02 / MY JOURNEY</span>
                    <h2 class="section-title">Education</h2>
                    <p class="section-description">
                        My educational background and academic journey.
                    </p>
                    <div class="heading-line"></div>
                </div>

                <div class="education-timeline">

                    <article class="card education-card">
                        <span class="education-year">2025–2029</span>
                        <div class="card-icon" aria-hidden="true">🎓</div>
                        <h3>Tertiary Education</h3>
                        <p>
                            <strong>Torres Capitol College, Inc.</strong>
                        </p>
                        <p>Bachelor of Science in Information Technology</p>
                    </article>

                    <article class="card education-card">
                        <span class="education-year">2019–2025</span>
                        <div class="card-icon" aria-hidden="true">📘</div>
                        <h3>Secondary Education</h3>
                        <p>
                            <strong>Dangcagan National High School</strong>
                        </p>
                    </article>

                    <article class="card education-card">
                        <span class="education-year">2013–2019</span>
                        <div class="card-icon" aria-hidden="true">📚</div>
                        <h3>Primary Education</h3>
                        <p>
                            <strong>Dangcagan Central Elementary School</strong>
                        </p>
                    </article>

                </div>
            </section>

            <!-- SKILLS -->
            <section class="section" id="skills">
                <div class="section-heading">
                    <span class="section-number">03 / WHAT I DO</span>
                    <h2 class="section-title">Skills and Interests</h2>
                    <p class="section-description">
                        Skills and areas I am interested in learning and developing.
                    </p>
                    <div class="heading-line"></div>
                </div>

                <div class="skill-grid">

                    <article class="skill-card">
                        <div class="skill-icon" aria-hidden="true">💻</div>
                        <h3>Python Programming</h3>
                        <p>Programming</p>
                    </article>

                    <article class="skill-card">
                        <div class="skill-icon" aria-hidden="true">🧩</div>
                        <h3>Problem Solving</h3>
                        <p>Logical thinking</p>
                    </article>

                    <article class="skill-card">
                        <div class="skill-icon" aria-hidden="true">🧠</div>
                        <h3>Critical Thinking</h3>
                        <p>Analysis and reasoning</p>
                    </article>

                    <article class="skill-card">
                        <div class="skill-icon" aria-hidden="true">📖</div>
                        <h3>Reading Comprehension</h3>
                        <p>Reading and understanding</p>
                    </article>

                    <article class="skill-card">
                        <div class="skill-icon" aria-hidden="true">🎨</div>
                        <h3>UI/UX Design</h3>
                        <p>Design and layout</p>
                    </article>

                    <article class="skill-card">
                        <div class="skill-icon" aria-hidden="true">⚙️</div>
                        <h3>Interactive Applications</h3>
                        <p>Application development</p>
                    </article>

                </div>
            </section>

            <!-- CERTIFICATES -->
            <section class="section" id="certificates">
                <div class="section-heading">
                    <span class="section-number">04 / ACHIEVEMENTS</span>
                    <h2 class="section-title">Certificates</h2>
                    <p class="section-description">
                        Certificates and learning achievements.
                    </p>
                    <div class="heading-line"></div>
                </div>

                <div class="certificate-gallery">
                    <div class="certificate-frame">
                        <img
                            src="{{ url_for('static', filename='images/jhulian.png') }}"
                            alt="Certificate 1"
                            loading="lazy"
                        >
                    </div>

                    <div class="certificate-frame">
                        <img
                            src="{{ url_for('static', filename='images/claire.png') }}"
                            alt="Certificate 2"
                            loading="lazy"
                        >
                    </div>
                </div>
            </section>

            <!-- PROJECTS: STUDENTS' ALLOWANCE TRACKER SYSTEM -->
            <section class="section" id="projects">
                <div class="section-heading">
                    <span class="section-number">05 / MY WORK</span>
                    <h2 class="section-title">My Projects</h2>
                    <p class="section-description">
                        Here is a system I developed to help students
                        manage their allowance and track their expenses.
                    </p>
                    <div class="heading-line"></div>
                </div>

                <div class="card-grid">
                    <article class="card">
                        <div class="card-icon" aria-hidden="true">💰</div>

                        <h3>Students' Allowance Tracker System</h3>

                        <p>
                            A web-based system designed to help students
                            manage their allowance, record daily expenses,
                            monitor their remaining balance, and review
                            their spending history and summaries.
                        </p>

                        <p style="margin-top: 15px;">
                            <strong>Technologies:</strong>
                            HTML, CSS, JavaScript, and localStorage
                        </p>

                        <a
                            class="primary-button"
                            href="https://allowancetrackingsystem.netlify.app/"
                            target="_blank"
                            rel="noopener noreferrer"
                            style="margin-top: 20px;"
                        >
                            Open Allowance Tracker System ↗
                        </a>
                    </article>
                </div>
            </section>

            <!-- SOCIAL MEDIA -->
            <section class="section" id="social">
                <div class="section-heading">
                    <span class="section-number">06 / CONNECT</span>
                    <h2 class="section-title">Social Media</h2>
                    <p class="section-description">
                        You can find me on these social media platforms.
                    </p>
                    <div class="heading-line"></div>
                </div>

                <div class="social-links">
                    <a
                        href="https://www.facebook.com/jhulian.claire.andoy"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        <span class="social-icon" aria-hidden="true">ⓕ</span>
                        <span class="social-name">Facebook ↗</span>
                    </a>

                    <a
                        href="https://www.instagram.com/julyankler"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        <span class="social-icon" aria-hidden="true">◎</span>
                        <span class="social-name">Instagram ↗</span>
                    </a>

                    <a
                        href="https://www.tiktok.com/@julyankler"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        <span class="social-icon" aria-hidden="true">♪</span>
                        <span class="social-name">TikTok ↗</span>
                    </a>
                </div>

                <div class="closing-card">
                    <p class="eyebrow">Thank you for visiting</p>
                    <h3>
                        Keep Learning.<br>
                        <span class="gradient-text">Keep Growing.</span>
                    </h3>
                    <p>
                        Every step is an opportunity to learn something new.
                    </p>
                </div>
            </section>
        </main>

        <footer>
            <p>
                © 2026 <span class="footer-name">Jhulian Claire B. Andoy</span>
                | Personal Portfolio
            </p>
            <p>Designed with creativity and a love for technology.</p>
        </footer>
    </div>

    <button
        class="back-to-top"
        id="backToTop"
        onclick="scrollToSection('home')"
        aria-label="Back to top"
        title="Back to top"
    >↑</button>

    <script>
        function openPortfolio() {
            document.getElementById("welcome").style.display = "none";
            document.getElementById("dashboard").style.display = "block";
            document.getElementById("backToTop").style.display = "flex";

            window.scrollTo({
                top: 0,
                behavior: "auto"
            });

            updateProgress();
        }

        function returnToWelcome() {
            document.getElementById("dashboard").style.display = "none";
            document.getElementById("welcome").style.display = "flex";
            document.getElementById("backToTop").style.display = "none";

            window.scrollTo({
                top: 0,
                behavior: "auto"
            });

            updateProgress();
        }

        function scrollToSection(sectionId) {
            const section = document.getElementById(sectionId);

            if (section) {
                section.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        }

        function updateProgress() {
            const dashboard = document.getElementById("dashboard");
            const bar = document.getElementById("progressBar");
            const backToTop = document.getElementById("backToTop");

            if (dashboard.style.display === "none") {
                bar.style.width = "0%";
                return;
            }

            const scrollableHeight =
                document.documentElement.scrollHeight - window.innerHeight;

            const progress = scrollableHeight > 0
                ? (window.scrollY / scrollableHeight) * 100
                : 0;

            bar.style.width =
                Math.min(100, Math.max(0, progress)) + "%";

            if (window.scrollY > 350) {
                backToTop.style.display = "flex";
            } else {
                backToTop.style.display = "none";
            }
        }

        window.addEventListener("scroll", updateProgress);
        window.addEventListener("resize", updateProgress);
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5003,
        debug=True
    )
